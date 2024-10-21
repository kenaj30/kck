import pandas as pd
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
tabela = pd.read_csv("big.dem",skiprows=1,header=None, sep=" ")
tabela = tabela.iloc[:,:-1]
tabela = pd.DataFrame(scaler.fit_transform(tabela), columns=tabela.columns)
print(tabela)