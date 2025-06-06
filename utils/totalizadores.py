from dados.compras import df
import pandas as pd
import streamlit as st
import re
from datetime import date

# Data atual
hoje = date.today()





#Calculo da ultima e menor data do sistema
#ultima_data =  df['data'].max()
#primeira_data =  df['data'].min()


# Calculo da quantidade de pontos de wifi
totalOpcoesCompras = df.shape[0]
totalBairro = df['Bairro'].count()

# criar o df para zonas e bairros
df_zona = df.groupby('Região')[['Bairro']].count().reset_index()
df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False)
df_mapa = df[['Bairro', 'Latitude', 'Longitude' ]]
df_opcao = df.groupby('Opção').size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False)