import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.title('Análise de veículos')

col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Criar histograma')
    if hist_button:
        st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
        fig = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    scatter_button = st.button('Criar gráfico de dispersão')
    if scatter_button:
        st.write('Criando um gráfico de dispersão para os dados de carros')
        fig_scatter = px.scatter(car_data, x="odometer", y="price", color="model")
        st.plotly_chart(fig_scatter, use_container_width=True)
