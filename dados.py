import pandas as pd

BancoDeDados = pd.read_csv("GraficosPrazoGS.xlsx - BD.csv")
riscos_baixos = BancoDeDados[BancoDeDados["Unnamed: 4"] == "Baixo"]
contagem_por_loja = riscos_baixos["Unnamed: 6"].value_counts()

print(contagem_por_loja)

