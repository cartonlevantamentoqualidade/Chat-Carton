import streamlit as st
from consulta_of import consultar_of
from indicador_data import indicador_por_data

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================

st.set_page_config(
    page_title="Chat Carton",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Chat Carton")
st.write("Bem-vindo ao sistema da Carton.")

# ==========================
# MENU LATERAL
# ==========================

st.sidebar.title("Menu")

pagina = st.sidebar.radio(
    "Escolha uma opção",
    [
        "Consulta OF",
        "Indicador por Data"
    ]
)

# ==========================================================
# CONSULTA OF
# ==========================================================

if pagina == "Consulta OF":

    st.header("📋 Consulta de Ordem de Fabricação")

    numero = st.text_input("Digite o número da OF")

    if st.button("Consultar"):

        if numero == "":
            st.warning("Digite uma OF.")
        else:

            resultado = consultar_of(numero)

            if resultado is None:

                st.error("OF não encontrada!")

            else:

                st.success("OF encontrada!")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Dados Gerais")

                    st.write(f"**OF:** {resultado['OF']}")
                    st.write(f"**Cliente:** {resultado['Cliente']}")
                    st.write(f"**Data:** {resultado['Data'].strftime('%d/%m/%Y')}")
                    st.write(f"**Turno:** {resultado['Turno']}")

                with col2:
                    st.subheader("Controle")

                    st.metric(
                        "Apontamentos",
                        resultado["Apontamentos"]
                    )

                st.divider()

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Peso Produzido",
                    f"{resultado['Peso']:,.2f} KG"
                )

                col2.metric(
                    "M² Produzido",
                    f"{resultado['M2']:,.2f}"
                )

                col3.metric(
                    "Metros Lineares",
                    f"{resultado['Metros']:,.2f}"
                )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("Processo")

                    st.metric(
                        "Refile",
                        f"{resultado['Refile']:,.2f} KG"
                    )

                    st.metric(
                        "% Refile",
                        f"{resultado['% Refile']:.2f}%"
                    )

                with col2:

                    st.subheader("Financeiro")

                    st.metric(
                        "Valor Produzido",
                        f"R$ {resultado['Valor']:,.2f}"
                    )

                    st.metric(
                        "Preço Médio KG",
                        f"R$ {resultado['Preço KG']:,.2f}"
                    )

# ==========================================================
# INDICADOR POR DATA
# ==========================================================

elif pagina == "Indicador por Data":

    st.header("📊 Indicador Diário")

    data = st.date_input(
        "Escolha uma data",
        format="DD/MM/YYYY"
    )

    if st.button("Gerar Indicador"):

        with st.spinner("Gerando indicador..."):

            resultado = indicador_por_data(data)

        if resultado is None:

            st.error("Nenhum apontamento encontrado para esta data.")

        else:

            st.success("Indicador gerado com sucesso!")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "OF Produzidas",
                    resultado["OF"]
                )

                st.metric(
                    "Apontamentos",
                    resultado["Apontamentos"]
                )

                st.metric(
                    "Peso Produzido",
                    f"{resultado['Peso']:,.2f} KG"
                )

                st.metric(
                    "Área Produzida",
                    f"{resultado['M2']:,.2f} m²"
                )

            with col2:

                st.metric(
                    "Metros Lineares",
                    f"{resultado['Metros']:,.2f}"
                )

                st.metric(
                    "Valor Produzido",
                    f"R$ {resultado['Valor']:,.2f}"
                )

                st.metric(
                    "Preço Médio KG",
                    f"R$ {resultado['Preço KG']:,.2f}"
                )

                st.metric(
                    "% Refile",
                    f"{resultado['% Refile']:.2f}%"
                )

            st.divider()

            st.metric(
                "Refile Total",
                f"{resultado['Refile']:,.2f} KG"
            )