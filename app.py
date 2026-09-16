import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.title('Análise de veículos')
st.subheader('Descrição do projeto')
st.write(
    'Este projeto usa Streamlit e Plotly Express para explorar dados de anúncios de veículos usados. '
    'A interface permite visualizar padrões de odômetro, preço e distribuição por modelo de forma interativa.'
)
st.write('Nele é possível:')
st.write('- visualizar histogramas para a coluna de odômetro;')
st.write('- gerar gráficos de dispersão entre odômetro e preço;')
st.write('- explorar os dados com uma interface simples e funcional.')

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
        fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition")
        st.plotly_chart(fig_scatter, use_container_width=True)
