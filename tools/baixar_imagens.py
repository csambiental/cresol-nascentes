"""Baixa mosaicos de satélite e rios do OpenStreetMap para a abertura do vídeo
(efeito Earth Zoom sobre Londrina). Tenta várias fontes abertas, em paralelo, com tempo curto."""
import math, os, json, io, time, sys, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
LAT, LON = -23.31, -51.16
OUT = "video-assets"
os.makedirs(OUT, exist_ok=True)
SOURCES = [
    ("eox2016", "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2016_3857/default/g/{z}/{y}/{x}.jpg", 14,
     "Sentinel-2 cloudless 2016 – s2maps.eu by EOX IT Services GmbH (contém dados Copernicus Sentinel modificados), CC BY 4.0"),
    ("gibs", "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/BlueMarble_ShadedRelief_Bathymetry/default/GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpeg", 8,
     "NASA Blue Marble (NASA GIBS), domínio público"),
    ("esri", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", 19,
     "Esri World Imagery – Esri, Maxar, Earthstar Geographics"),
]
UA = {"User-Agent": "cresol-nascentes-video/1.0 (github.com/csambiental/cresol-nascentes)"}
def get(url, tries=2, timeout=20):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
        except Exception as e:
            err = e; time.sleep(1)
    print("  falhou", url[:90], type(err).__name__, err, flush=True)
    return None
def tile_xy(lat, lon, z):
    n = 2 ** z
    return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
# teste rápido de cada fonte
alive = []
for name, url, zmax, attr in SOURCES:
    x, y = tile_xy(LAT, LON, 6)
    b = get(url.format(z=6, x=int(x), y=int(y)), tries=1, timeout=15)
    ok = bool(b) and len(b) > 1000
    print("fonte", name, "OK" if ok else "indisponível", flush=True)
    if ok: alive.append((name, url, zmax, attr))
if not alive: sys.exit("nenhuma fonte de imagem respondeu")
meta, used = {}, set()
GRID = 8
pool = ThreadPoolExecutor(16)
for z in range(2, 15):
    src = next((s for s in alive if s[2] >= z), None)
    if not src: continue
    name, url, zmax, attr = src
    cx, cy = tile_xy(LAT, LON, z)
    n = 2 ** z; g = min(GRID, n)
    x0 = max(0, min(n - g, int(math.floor(cx - g / 2)))); y0 = max(0, min(n - g, int(math.floor(cy - g / 2))))
    jobs = [(i, j, url.format(z=z, x=x0 + i, y=y0 + j)) for j in range(g) for i in range(g)]
    res = list(pool.map(lambda t: (t[0], t[1], get(t[2])), jobs))
    im = Image.new("RGB", (256 * g, 256 * g), (8, 20, 30)); got = 0
    for i, j, b in res:
        if b:
            try: im.paste(Image.open(io.BytesIO(b)).convert("RGB"), (i * 256, j * 256)); got += 1
            except Exception: pass
    im.save(f"{OUT}/z{z:02d}.jpg", quality=88)
    meta[z] = {"x0": x0, "y0": y0, "g": g, "cx": cx, "cy": cy, "fonte": name}
    used.add(attr)
    print("z", z, name, f"{got}/{len(jobs)}", flush=True)
json.dump({"center": [LAT, LON], "levels": meta, "attribution": " · ".join(sorted(used))},
          open(f"{OUT}/mosaicos.json", "w"), indent=1, ensure_ascii=False)
# rios e córregos (OSM)
q = '[out:json][timeout:120];(way["waterway"~"^(river|stream)$"](-23.80,-51.50,-22.95,-50.80););out geom;'
data = None
for ep in ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter"]:
    b = get(ep + "?data=" + urllib.parse.quote(q), tries=2, timeout=150)
    if b:
        try: data = json.loads(b); break
        except Exception: pass
feats = []
for el in (data or {}).get("elements", []):
    if "geometry" in el:
        feats.append({"type": "Feature", "properties": {"waterway": el.get("tags", {}).get("waterway"), "name": el.get("tags", {}).get("name", "")},
                      "geometry": {"type": "LineString", "coordinates": [[round(p["lon"], 5), round(p["lat"], 5)] for p in el["geometry"]]}})
json.dump({"type": "FeatureCollection", "attribution": "© OpenStreetMap contributors (ODbL)", "features": feats},
          open(f"{OUT}/rios.geojson", "w"))
print("rios", len(feats), flush=True)
