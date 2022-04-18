import pandas as pd
import math

partidas = pd.read_csv("dados/2018/Partidas/2018_partidas.csv")

#for x in rodadas:

"""
instancias = pd.DataFrame(columns= [
"atletas.posicao_id",
"atletas.rodada_id",
"atletas.pontos_num",
"atletas.preco_num",
"atletas.variacao_num",
"atletas.media_num",
"FC",
"FD",
"FF",
"FS",
"G" ,
"I" ,
"RB",
"CA",
"PE",
"A" ,
"SG",
"DD",
"FT",
"GS",
"CV",
"GC",

"i.FC",
"i.FD",
"i.FF",
"i.FS",
"i.G" ,
"i.I" ,
"i.RB",
"i.CA",
"i.PE",
"i.A" ,
"i.SG",
"i.DD",
"i.FT",
"i.GS",
"i.CV",
"i.GC",
])
"""

#print(partidas.columns)
#print(pd.concat( [partidas[partidas["home_team"] == "Atlético-PR"],partidas[partidas["away_team"] == "Atlético-PR"]],axis=0))
#print(rodada.index[rodada["atletas.clube.id.full.name"] == "Atlético-PR"].tolist())

#for index, row in rodada.iterrows():
    ## Pegar o time desse jogador

instances = {
"atletas.posicao_id": [],
"atletas.rodada_id": [],
"atletas.pontos_num": [],
"atletas.preco_num": [],
"atletas.variacao_num": [],
"atletas.media_num": [],
"FC": [],
"FD": [],
"FF": [],
"FS": [],
"G" : [],
"I" : [],
"RB": [],
"CA": [],
"PE": [],
"A" : [],
"SG": [],
"DD": [],
"FT": [],
"GS": [],
"CV": [],
"GC": [],

"i.FC": [],
"i.FD": [],
"i.FF": [],
"i.FS": [],
"i.G" : [],
"i.I" : [],
"i.RB": [],
"i.CA": [],
"i.PE": [],
"i.A" : [],
"i.SG": [],
"i.DD": [],
"i.FT": [],
"i.GS": [],
"i.CV": [],
"i.GC": [], 
}

## Mapa de quem vai contra quem
positionMap = {
    #"zag": ["ata","mei","lat"],
    #"lat": ["ata","mei","zag"],
    "zag": ["ata","mei","zag","gol"],
    "lat": ["ata","mei","zag","gol"],
    "mei": ["ata","mei","zag","gol"],
    "ata": ["ata","mei","zag","gol"],
    "gol": ["ata","mei","zag","gol"],
    #"gol": ["ata","mei"],
}

for i in range(1,39):
    print(f"Rodada {i}")
    rodada = pd.read_csv(f"dados/2018/Rodadas/rodada-{i}.csv")
    for index, row in rodada.iterrows():
        ## Pegar time do jogador
        time = row["atletas.clube.id.full.name"]
        ## Pegar rodada atual
        rodadaId = row["atletas.rodada_id"]

        ## Pegar posição do jogador
        position = row["atletas.posicao_id"]
        if position == "tec":
            continue

        if not ((row["atletas.status_id"] == "Provável") or (row["atletas.pontos_num"] != 0)):
            continue

        ## Pegar todas as partidas dos filmes
        partidasDoTime = pd.concat( [partidas[partidas["home_team"] == time],partidas[partidas["away_team"] == time]],axis=0)

        ## Pegar o outro time
        outroTime = partidasDoTime[ partidasDoTime["round"] == rodadaId ].iloc[0]["home_team"] \
            if partidasDoTime[ partidasDoTime["round"] == rodadaId ].iloc[0]["home_team"] != time \
            else partidasDoTime[ partidasDoTime["round"] == rodadaId ].iloc[0]["away_team"]

        ## Pegar os jogadores ativos do outro time
        outrosJogadores = rodada[rodada["atletas.clube.id.full.name"] == outroTime] \
                                [ (rodada["atletas.status_id"] == "Provável") | (rodada["atletas.pontos_num"] != 0) ] \
                                [ rodada["atletas.posicao_id"].isin( positionMap[position] ) ]

        ## Adicionar dados do jogador
        for p in ["atletas.posicao_id", "atletas.rodada_id", "atletas.pontos_num", \
                "atletas.preco_num", "atletas.variacao_num", "atletas.media_num"]:  
            instances[p].append(row[p])

        ## Adicionar scouts do jogador
        for p in ["FC","FD","FF","FS","G" ,"I" ,"RB","CA","PE","A" ,"SG","DD","FT","GS","CV","GC"]:
            instances[p].append( (0 if math.isnan(row[p]) else row[p]) / rodadaId)

        ## Adicionar os scouts dos inimigos
        for p in ["FC","FD","FF","FS","G" ,"I" ,"RB","CA","PE","A" ,"SG","DD","FT","GS","CV","GC"]:
            instances["i."+p].append( sum(map(lambda a: 0 if math.isnan(a) else a ,outrosJogadores[p].tolist() ))/rodadaId )

df = pd.DataFrame(instances)
df.to_csv("dados/2018/Datasets/df.csv")


#print(sum(map(lambda a: 0 if math.isnan(a) else a ,outrosJogadores['GS'].tolist() )))
#print(outrosJogadores)

