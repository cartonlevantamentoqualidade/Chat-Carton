import pandas as pd

arquivo = "data/excel/previsão onduladeira v1,1.xlsx"

# Carrega a planilha apenas uma vez
df = pd.read_excel(
    arquivo,
    sheet_name="BASE DE DADOS",
    engine="openpyxl"
)

df.columns = df.columns.str.strip()
df["of"] = df["of"].astype(str).str.strip()


def consultar_of(of_digitada):

    of_digitada = str(of_digitada).strip()

    resultado = df[df["of"] == of_digitada]

    if resultado.empty:
        return None

    peso = resultado["PESO"].sum()
    m2 = resultado["M²"].sum()
    metros = resultado["METROS LINEAR"].sum()
    refile = resultado["REFILE KG"].sum()
    valor = resultado["VALOR ITEN"].sum()

    preco_kg = valor / peso if peso > 0 else 0

    primeira_linha = resultado.iloc[0]

    cliente = primeira_linha["CLIENTE"]
    if pd.isna(cliente):
        cliente = "Não informado"

    percentual_refile = (refile / peso) * 100 if peso > 0 else 0

    return {
        "OF": of_digitada,
        "Cliente": cliente,
        "Data": primeira_linha["data"],
        "Turno": primeira_linha["TURNO"],
        "Peso": peso,
        "M2": m2,
        "Metros": metros,
        "Refile": refile,
        "% Refile": percentual_refile,
        "Valor": valor,
        "Preço KG": preco_kg,
        "Apontamentos": len(resultado)
    }
