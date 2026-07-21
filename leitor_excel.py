import pandas as pd
import os

PASTA = "data/excel"

def carregar_planilhas():
    dados = {}

    for arquivo in os.listdir(PASTA):
        if arquivo.endswith(".xlsx"):
            caminho = os.path.join(PASTA, arquivo)
            df = pd.read_excel(caminho)
            dados[arquivo] = df

    return dados


if __name__ == "__main__":
    planilhas = carregar_planilhas()

    for nome, df in planilhas.items():
        print(f"\nPlanilha: {nome}")
        print(df.head())