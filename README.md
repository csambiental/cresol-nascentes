# Nascentes de Londrina – simulação

Mapa demonstrativo de controle e transparência das nascentes vistoriadas em Londrina.

Realização: Cresol · Execução: CS Consultoria Ambiental · Apoio: Instituto Biosimos

**Este repositório é uma simulação.** Os 42 pontos, as coordenadas e as fichas (bacia, bairro, diagnóstico, recomendações e laudo fotográfico) foram transcritos do laudo de vistoria do Projeto Broto d'Água. As situações são ilustrativas.

| Situação | Pontos |
|---|---|
| Executadas | 20 |
| Em análise | 15 |
| Não aptas | 5 (nascentes canalizadas: 7, 14, 31, 35, 37) |
| Localização a confirmar | 1 (ponto 39: a coordenada do laudo repete a do ponto 36; usada posição aproximada na UEL) |
| Sem coordenada | 1 (ponto 13: ficha não disponível) |

Os pontos 17 e 21 têm a mesma coordenada no laudo e aparecem sobrepostos.

## Arquivos

- `index.html` – mapa (satélite ou ruas), filtros por situação, lista dos pontos e ficha completa de cada nascente
- `data/nascentes.json` – um registro por ponto: `ponto, nome, bacia, bairro, lat, lon, situacao, diagnostico[], recomendacoes[], laudo_fotografico, nota`

Situações aceitas: `executada`, `em_analise`, `nao_apta`, `a_confirmar`, `sem_coordenada`.

## Ver o mapa

https://csambiental.github.io/cresol-nascentes/

Nenhum dado pessoal é publicado neste repositório.
