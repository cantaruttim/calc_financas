import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
valor = os.getenv("VALOR")

caminho = "./dados"
investimentos = f"{caminho}/Controle de Gastos.xlsx"
sheet = "Investimentos"

df = pd.read_excel(
    investimentos, 
    sheet_name=sheet, 
    engine="openpyxl"
)

df["acumulado_investido"] = df["Valor"].sum()
print(df)