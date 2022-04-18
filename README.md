# Modelo Preditivo Cartola FC

## Modelo Defesa

Para a defesa será feito da seguinte maneira: 

- serão excluidos jogadores:
  - "atletas.posicao_id" != "zag"
  - "atletas.status_id" != "Provável"
- NA é substituido por 0
- Serão utilizado os parametros do atleta:
  - "atletas.rodada_id"
  - "atletas.pontos_num"
  - "atletas.preco_num"
  - "atletas.variacao_num"
  - "atletas.media_num"
  - "FC" Faltas Cometidas
  - "FD" Finalizações Defendidas
  - "FF" Finalizações para Fora
  - "FS" Faltas Sofridas
  - "G"  Gols
  - "I" Impedimentos
  - "RB" Roubadas de Bola
  - "CA" Cartões amarelos
  - "PE" Passes Errados
  - "A" Assistencias
  - "SG" Jogos sem Sofrer Gols
  - "DD" Defesas Dificeis
  - "FT" Finalizações na Trave
  - "GS" Gols Sofridos
  - "CV" Cartões vermelhos
  - "GC" Gols Contra
- Os Parametros do time adversário serão a soma de todos os atacantes dos parametros:
  - "FC" Faltas Cometidas
  - "FD" Finalizações Defendidas
  - "FF" Finalizações para Fora
  - "FS" Faltas Sofridas
  - "G"  Gols
  - "I" Impedimentos
  - "RB" Roubadas de Bola
  - "CA" Cartões amarelos
  - "PE" Passes Errados
  - "A" Assistencias
  - "SG" Jogos sem Sofrer Gols
  - "DD" Defesas Dificeis
  - "FT" Finalizações na Trave
  - "GS" Gols Sofridos
  - "CV" Cartões vermelhos
  - "GC" Gols Contra

Objetivo pode ser tanto a "variacao_num" quanto "atletas.pontos_num"

Uma instancia é composta pelos scouts do jogador e a soma dos scouts dos inimigos diretos.

Inimigos diretos:

- zag → ata
- zag → mei
- lat → ata
- lat → mei
- lat → zag
- mei → ata
- mei → mei
- mei → zag
- ata → zag
- ata → mei
