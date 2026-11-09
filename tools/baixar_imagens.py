"""Baixa mosaicos Sentinel-2 cloudless 2016 (EOX, CC BY 4.0) e rios do OpenStreetMap
para a abertura do vídeo (efeito Earth Zoom sobre Londrina)."""
import math, os, json, io, time, urllib.request, urllib.parse
from PIL import Image
LAT, LON = -23.31, -51.16
OUT = "video-assets"
os.makedirs(OUT, exist_ok=True)
URL = "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2016_3857/default/g/{z}/{y}/{x}.jpg"
def tile_xy(lat, lon, z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y
def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "cresol-nascentes-video/1.0"})
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            time.sleep(2 + i * 2)
    return None
meta = {}
GRID = 8
for z in range(2, 15):
    cx, cy = tile_xy(LAT, LON, z)
    n = 2 ** z
    g = min(GRID, n)
    x0 = int(math.floor(cx - g / 2)); y0 = int(math.floor(cy - g / 2))
    x0 = max(0, min(n - g, x0)); y0 = max(0, min(n - g, y0))
    im = Image.new("RGB", (256 * g, 256 * g), (8, 20, 30))
    for j in range(g):
        for i in range(g):
            b = get(URL.format(z=z, x=x0 + i, y=y0 + j))
            if b:
                try: im.paste(Image.open(io.BytesIO(b)).convert("RGB"), (i * 256, j * 256))
                except Exception: pass
    im.save(f"{OUT}/z{z:02d}.jpg", quality=88)
    meta[z] = {"x0": x0, "y0": y0, "g": g, "cx": cx, "cy": cy}
    print("z", z, "ok")
json.dump({"center": [LAT, LON], "levels": meta,
           "attribution": "Sentinel-2 cloudless 2016 – s2maps.eu by EOX IT Services GmbH (contains modified Copernicus Sentinel data 2016), CC BY 4.0"},
          open(f"{OUT}/mosaicos.json", "w"), indent=1)
# rios e córregos (OSM)
q = '[out:json][timeout:180];(way["waterway"~"^(river|stream)$"](-23.80,-51.50,-22.95,-50.80););out geom;'
data = None
for ep in ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]:
    b = get(ep + "?data=" + urllib.parse.quote(q))
    if b:
        data = json.loads(b); break
feats = []
if data:
    for el in data.get("elements", []):
        if "geometry" in el:
            feats.append({"type": "Feature", "properties": {"waterway": el.get("tags", {}).get("waterway"), "name": el.get("tags", {}).get("name", "")},
                          "geometry": {"type": "LineString", "coordinates": [[round(p["lon"], 5), round(p["lat"], 5)] for p in el["geometry"]]}})
json.dump({"type": "FeatureCollection", "attribution": "© OpenStreetMap contributors (ODbL)", "features": feats}, open(f"{OUT}/rios.geojson", "w"))
print("rios", len(feats))
