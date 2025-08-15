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

## Dados de investimentos
df = ler_investimentos(path_file, sheet)
df["acumulado_investido"] = df["Valor"].sum()
print(df.head(10))

print()

## Dados da Selic - Bacen
selic = ler_taxa_selic(taxa_selic)

def tratamentos_iniciais(df, columns):

    # Remove espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()

    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    

    cols = ["Taxa_aa", "Taxa_media", "Taxa_mediana", "Taxa_modal"]
    for col in cols:
        df[col] = df[col].str.replace(",", ".", regex=False).astype(float)

    return df

selic = tratamentos_iniciais(selic)
print(selic)