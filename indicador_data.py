from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
arquivo = "data/excel/previsão onduladeira v1,1.xlsx"

df = pd.read_excel(
    arquivo,
    sheet_name="BASE DE DADOS",
    engine="openpyxl"
)

df.columns = df.columns.str.strip()
df["data"] = pd.to_datetime(df["data"])


def indicador_por_data(data_consulta):

    data_consulta = pd.to_datetime(data_consulta)

    resultado = df[df["data"] == data_consulta]

    if resultado.empty:
        return None

    peso = resultado["PESO"].sum()
    m2 = resultado["M²"].sum()
    metros = resultado["METROS LINEAR"].sum()
    valor = resultado["VALOR ITEN"].sum()
    refile = resultado["REFILE KG"].sum()

    qtd_of = resultado["of"].nunique()
    apontamentos = len(resultado)

    preco_kg = valor / peso if peso > 0 else 0
    percentual_refile = (refile / peso) * 100 if peso > 0 else 0

    return {
        "Data": data_consulta,
        "Peso": peso,
        "M2": m2,
        "Metros": metros,
        "Valor": valor,
        "Preço KG": preco_kg,
        "Refile": refile,
        "% Refile": percentual_refile,
        "OF": qtd_of,
        "Apontamentos": apontamentos
    }
