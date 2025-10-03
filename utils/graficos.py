import matplotlib as pl
import plotly.express as px
import streamlit as st
import pandas as pd
from utils.totalizadores import df_bairro, df_zona, df_mapa, df_opcao




    
#Criando o gráfico de distribuicao por zona
def grafico_zona(df):
        df_agrupado = df.groupby('Região')[['Bairro']].count().reset_index()
        
        fig =  px.treemap(
            df_agrupado,
            path=['Região'],
            values='Bairro',
            color='Bairro',
            
        )
        fig.update_layout(
            title={
                'text': 'Centro de compras por região da cidade',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    
                }
            }
        )
        return fig
    # gerar os graficos a partir do df filtrado

    
    # Criando o gráfico de distribuicao por bairro
def grafico_bairro(df):
        df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL')
        df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

        fig1 =  px.bar(
            df_bairro,
            x='Bairro',
            y='TOTAL',
            
        )
        fig1.update_layout(
            title={
                'text': 'Centro de compras por bairro',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                   
                }
            }
        )
        return fig1

def grafico_opcao(df):
        df_bairro = df.groupby('Opção').size().reset_index(name='TOTAL')
        df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

        fig4 =  px.bar(
            df_bairro,
            x='Opção',
            y='TOTAL',
            
        )
        fig4.update_layout(
            title={
                'text': 'Opções de centros de compras',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    
                }
            }
        )
        return fig4

    # Criando o gráfico de distribuicao por mapa
def grafico_mapa(df):
    fig3 = px.scatter_mapbox(
        df,
        hover_name='Nome',
        hover_data={
            'Opção': True,
            'Região': True,
            'Bairro': True,
            'Funcionamento': True,
            'Localização': True
        },
        lat='Latitude',
        lon='Longitude',
        color='Opção',  # ← as cores agora representam os valores da coluna 'Opção'
        zoom=11,
        height=500
    )

    # Aumenta o tamanho das bolinhas
    fig3.update_traces(marker=dict(size=15))  # ajuste o valor conforme necessário

    fig3.update_layout(
        title={
            'text': 'Principais centros de compras na cidade do Recife',
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 22,
                
            }
        }
    )

    return fig3


