import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.totalizadores import df_bairro, df_zona, df_mapa, df_opcao
#from funcoes import df_bairro, df_zona, df_mapa



    
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
                    'color': '#0b3d91'
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
                    'color':  '#0b3d91'
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
                    'color':  '#0b3d91'
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
                'color': '#0b3d91'
            }
        }
    )

    return fig3


def mainGraficos(df_filtrado):

    st.markdown("<hr style='border:2px solid #0b3d91;'>", unsafe_allow_html=True)

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    fig_opcao = grafico_opcao(df_filtrado)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(figura_zona, use_container_width=True ) #config={"displayModeBar": False})
    with col2:
        st.plotly_chart(figura_bairro, use_container_width=True, stack=False)
    with col3:
        st.plotly_chart(fig_opcao, use_container_width=True, stack=False)

    st.markdown("<hr style='border:2px solid #0b3d91;'>", unsafe_allow_html=True)

    fig_mapa.update_layout(mapbox_style="open-street-map")
    fig_mapa.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

    # Aplica a margem com a div
    st.markdown('<div class="grafico-com-margem">', unsafe_allow_html=True)
    st.plotly_chart(fig_mapa, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)