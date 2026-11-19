import streamlit as st 
import pandas as pd
import plotly.express as px
import openpyxl
import python_calamine

df = pd.read_csv("censo_1872.csv")
df = df.drop_duplicates ()

df_filtrado = df[
    (df["homens_livres"]) &
    (df["homens_escravizados"])
    (df["mulheres_livres"]) &
    (df["mulheres_escravizadas"])
].copy()

df_filtrado = df[
    (df["total_livres"]) &
    (df["total_escravizados"])
].copy()

# Cria uma tabela menor somente com as colunas necessárias
# para os gráficos que utilizam ANO, bairro e IQVU.
df_tabela = df_filtrado[[ homens livres / (homens livres + homens escravizados)]]&
df_tabela = df_filtrado[[ homens escravizados / (homens livres + homens
escravizados)]]
df_tabela = df_filtrado[[ mulheres livres / (mulheres livres + mulheres escravizados)]]&
df_tabela = df_filtrado[[ mulheres escravizados / (mulheres livres + mulheres
escravizados)]].copy()


st.title("Painel do Censo Demográfico de 1872")

st.sidebar.header("Controles")
opcao = st.sidebar.radio(
    "Selecione a visualização:",
    ["Tabela", "Gráficos"]
)

if opcao == "Tabela":
    st.header("Tabela do Censo")

    st.dataframe(
        df_tabela,
        use_container_width=True,
        hide_index=True
    )

elif opcao == "Gráficos":

    st.header("Gráficos do Censo")

    st.subheader("Gráfico de Pizza Homens")

    dados_pizza = [["homens_livres,  homens_escravizados"]].copy()

    fig_pizza = px.pie(
        dados_pizza,
        names="homens_livres",
        values="homens_escravizados",
        color="ano",
        title="Percentual de homens livres e homens escravizados",
        color_discrete_map={
            "homens_livres": "#FF6B6B",
            "homens_escravizados": "#00F5D4"
        },
        template="plotly_dark"
    )

    fig_pizza.update_traces(
        textinfo="percent+label+value"
    )

    st.plotly_chart(
        fig_pizza,
        use_container_width=True
    )

    st.subheader("Gráfico de Pizza Mulheres")

    dados_pizza = [["mulheres_livres,  mulheres_escravizadas"]].copy()

    fig_pizza = px.pie(
        dados_pizza,
        names="mulheres_livres",
        values="mulheres_escravizadas",
        color="ano",
        title="Percentual de mulheres livres e mulheres escravizadas",
        color_discrete_map={
            "mulheres_livres": "#FF6B6B",
            "mulheres_escravizadas": "#00F5D4"
        },
        template="plotly_dark"
    )

    fig_pizza.update_traces(
        textinfo="percent+label+value"
    )

    st.plotly_chart(
        fig_pizza,
        use_container_width=True
    )

    st.markdown("---")

st.caption(
    "Fonte dos dados: https://basedosdados.org/"
)
