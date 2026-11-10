# Nascentes de Londrina – Ação de Proteção de Nascentes

Mapa de controle e transparência das nascentes de Londrina/PR: os 42 pontos do laudo de vistoria do Projeto Broto d'Água e as nascentes executadas pela Secretaria Municipal do Ambiente (SEMA).

Realização: Cresol · Execução: CS Consultoria Ambiental · Apoio: Instituto Biosimos

**Ver o mapa:** https://csambiental.github.io/cresol-nascentes/

## Fontes

- **Laudo de vistoria do Projeto Broto d'Água (Londrina)** – 42 pontos; coordenadas, bacia, bairro, diagnóstico, recomendações e referência ao laudo fotográfico transcritos do documento original.
- **Lista de nascentes executadas da SEMA Londrina** – 20 pontos com coordenadas, recebida em 10/11/2026. A SEMA é a fonte oficial destes dados.
- **Limite municipal** – IBGE (código 4113700).

## Dados abertos (pasta `dados/`)

Os mesmos dados do mapa, prontos para importar em sistemas de geoprocessamento (QGIS, ArcGIS, sistemas municipais). Coordenadas geográficas em SIRGAS 2000 / WGS 84 (graus decimais).

| Conjunto | CSV | GeoJSON | KML | Shapefile |
|---|---|---|---|---|
| Laudo Broto d'Água (42 pontos) | [csv](dados/nascentes_laudo_broto_dagua.csv) | [geojson](dados/nascentes_laudo_broto_dagua.geojson) | [kml](dados/nascentes_laudo_broto_dagua.kml) | [zip](dados/nascentes_laudo_broto_dagua_shp.zip) |
| Nascentes executadas pela SEMA (20 pontos) | [csv](dados/nascentes_executadas_sema.csv) | [geojson](dados/nascentes_executadas_sema.geojson) | [kml](dados/nascentes_executadas_sema.kml) | [zip](dados/nascentes_executadas_sema_shp.zip) |

Observações:
- CSV separado por ponto e vírgula, codificação UTF-8.
- No shapefile, os textos longos (diagnóstico e recomendações) ficam limitados a 254 caracteres pelo formato DBF; o texto completo está no CSV e no GeoJSON.
- O ponto 13 do laudo não tem coordenada e aparece só no CSV.

### Campos – laudo
`ponto, nome, bacia, bairro, situacao, itens_sema, lat, lon, laudo_foto, diagnostico, recomendacoes, nota`

`situacao`: Executada pela SEMA · A avaliar · Localização a confirmar · Sem coordenada. `itens_sema`: itens correspondentes na lista da SEMA.

### Campos – executadas pela SEMA
`item, local, ponto_laudo, lat, lon, nota`

`ponto_laudo`: ponto correspondente no laudo Broto d'Água (vazio quando fora do laudo).

## Notas de qualidade dos dados

- Laudo: ponto 39 com localização a confirmar (a coordenada do laudo repete a do ponto 36); pontos 17 e 21 com a mesma coordenada; ponto 13 sem ficha nem coordenada.
- Lista da SEMA: itens 1–3, 8–9 e 11–12 são pontos a poucos metros entre si (mesma nascente ou olhos d'água próximos). Corrigidos erros de digitação nos itens 15 (latitude sem ponto decimal), 17 (longitude sem ponto decimal) e 20 (longitude com vírgula).
- Cruzamento: 5 nascentes do laudo constam como executadas pela SEMA (pontos 11, 27, 29, 30 e 38).

## Arquivos do mapa

- `index.html` – mapa (satélite ou ruas), camadas com chave, legenda, lista com busca e ficha de cada ponto
- `data/nascentes.json`, `data/sema_executadas.json`, `data/limite_londrina.geojson` – dados usados pelo mapa
