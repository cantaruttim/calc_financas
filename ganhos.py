import pandas as pd
from gastos_cartao import (
    preencher_valores_faltantes, 
    comparativo_gastos, 
    aplicar_descontos,
    ler_arquivo_excel
)

caminho = "./dados"
gastos = f"{caminho}/Controle de Gastos.xlsx"
sheet = "Gastos_2025"

df = ler_arquivo_excel(caminho, sheet)
preencher_valores_faltantes(df)
