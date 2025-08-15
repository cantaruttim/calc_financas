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
        sep=","
    )
    return selic    

## Dados de investimentos
df = ler_investimentos(path_file, sheet)
df["acumulado_investido"] = df["Valor"].sum()
# print(df.info())

print()

## Dados da Selic - Bacen
selic = ler_taxa_selic(taxa_selic)
print(selic)

def trata_data(df, col):
    df[col] = pd.to_datetime(df[col], format= "%d/%m/%Y", errors='coerce')
    return df

def trata_valores(df, column_list: list):

    # Remover espaços extras dos nomes das colunas
    df.columns = df.columns.str.strip()

    # Verificar colunas ausentes
    for col in column_list:
        if col not in df.columns:
            raise KeyError(f"Coluna '{col}' não encontrada no DataFrame.")

    # Normalizar números
    df[column_list] = df[column_list].apply(
        lambda col: col.astype(str).str.replace(",", ".", regex=False).astype(float)
    )

    return df

selic = (
    trata_valores(
        trata_data(
            selic, 'Data'
        ), 
    column_list=[
        "Taxa_aa", 
        "Taxa_media", 
        "Taxa_mediana", 
        "Taxa_modal", 
        "Desvio_Padrao", 
        "Curtose"])
)



# selic2 = selic
# df = pd.merge(df, selic2, on='Data', how='left')
# print(df)

