# Nascentes de Londrina – simulação

Mapa demonstrativo de controle e transparência de nascentes protegidas em Londrina e região.

**Este repositório é uma simulação.** As localizações são reais; as situações "em análise" e "não apta" são ilustrativas.

| Situação | Pontos | Origem das localizações |
|---|---|---|
| Executadas | 20 | Pontos públicos divulgados pela Secretaria Municipal do Ambiente de Londrina (2025) |
| Em análise | 15 | Laudo do Projeto Broto d'Água (pontos 1, 2, 4, 6, 9, 10, 12, 22, 24, 25, 26, 28, 36, 40, 41) |
| Não aptas | 5 | Laudo do Projeto Broto d'Água – nascentes canalizadas (pontos 7, 14, 31, 35, 37) |

Pontos do laudo que coincidem com nascentes já executadas pela SEMA não foram repetidos.

## Arquivos

- `index.html` – mapa (satélite ou mapa de ruas), filtros por situação e lista de nascentes
- `data/nascentes.csv` – um ponto por linha: `id, situacao, endereco, bairro_distrito, lat, lon, fonte`

Situações aceitas: `executada`, `em_analise`, `nao_apta`.

## Ver o mapa

Settings › Pages › Branch `main`, pasta `/`. O mapa fica em `https://csambiental.github.io/cresol-nascentes/`.

Nenhum dado pessoal é publicado neste repositório.
