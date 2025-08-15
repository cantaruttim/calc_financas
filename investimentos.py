import pandas as pd
import os

caminho = "./dados"
path_file = f"{caminho}/Controle de Gastos.xlsx"
sheet = "Investimentos"
taxa_selic = f"{caminho}/taxa_selic_apurada.csv"


def ler_investimentos(path_file, sheet):

    df = pd.read_excel(
        path_file, 
        sheet_name=sheet, 
        engine="openpyxl"
    )
    return df

def ler_taxa_selic(path_file):
    selic = pd.read_csv(
        taxa_selic, 
        sep=";"
    )
    return selic    

df = ler_investimentos(path_file, sheet)
df["acumulado_investido"] = df["Valor"].sum()
print(df.head(10))

print()

selic = ler_taxa_selic(taxa_selic)
print(selic.head(10))

