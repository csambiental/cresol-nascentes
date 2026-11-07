# Nascentes de Londrina – simulação

Mapa demonstrativo de controle e transparência de nascentes protegidas em Londrina e região.

**Este repositório é uma simulação.** As situações dos pontos são ilustrativas e as localizações rurais são fictícias.

| Situação | Pontos | Origem das localizações |
|---|---|---|
| Executadas | 20 | Pontos públicos divulgados pela Secretaria Municipal do Ambiente de Londrina (2025) |
| Em análise | 15 | Simuladas em distritos rurais |
| Não aptas | 5 | Simuladas em distritos rurais |

## Arquivos

- `index.html` – mapa (satélite ou mapa de ruas), filtros por situação e lista de nascentes
- `data/nascentes.csv` – um ponto por linha: `id, situacao, endereco, bairro_distrito, lat, lon, fonte`

Situações aceitas: `executada`, `em_analise`, `nao_apta`.

## Ver o mapa

Settings › Pages › Branch `main`, pasta `/`. O mapa fica em `https://csambiental.github.io/cresol-nascentes/`.

Nenhum dado pessoal é publicado neste repositório.
