import pandas as pd
#from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor

df = pd.read_csv("dados/2018/Datasets/df.csv",index_col=0)

df = df[df["atletas.posicao_id"] == "ata"]
df = df[1:]
y = df["atletas.variacao_num"].tolist()

del df["atletas.variacao_num"]
del df["atletas.posicao_id"]

X = df.values.tolist()

model = MLPRegressor(hidden_layer_sizes=1000,activation="logistic",max_iter=500)
model.fit(X,y)
print(model.score(X,y))