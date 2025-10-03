import pandas as pd
import streamlit as st
from utils.graficos import grafico_bairro, grafico_mapa, grafico_opcao, grafico_zona
from utils.totalizadores import calcular_o_tamnnho_df, calcular_total_centro_compras



def mainDashboards(df_filtrado, df):
    
    st.markdown("<hr>", unsafe_allow_html=True)

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    fig_opcao = grafico_opcao(df_filtrado)

    total = calcular_o_tamnnho_df(df)    
    totalShopping = calcular_total_centro_compras(df,'Shopping')
    totalFeira = calcular_total_centro_compras(df, 'Feira popular')
    totalMercado = calcular_total_centro_compras(df, 'Mercado Público')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.container():
            st.metric(label="Total de Centros de Compras", value=total, border=True)
    with col2:
        with st.container():
            st.metric(label="Total de Shoppings", value=totalShopping, border=True)
    with col3:
        with st.container():
            st.metric(label="Total de Feira Livre", value=totalFeira, border=True)
    with col4:
        with st.container():
            st.metric(label="Total de Mercado Popular", value=totalMercado, border=True)
    

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(figura_zona, use_container_width=True, config={
            "displayModeBar": False,  # exemplo: esconde barra de ferramentas
            "scrollZoom": True        # habilita zoom com scroll
})
    with col2:
        st.plotly_chart(fig_opcao, use_container_width=True, config={
            "displayModeBar": False,  # exemplo: esconde barra de ferramentas
            "scrollZoom": True        # habilita zoom com scroll)
            }
        )
    st.plotly_chart(figura_bairro, use_container_width=True, config={
            "displayModeBar": False,  # exemplo: esconde barra de ferramentas
            "scrollZoom": True        # habilita zoom com scroll)
            }
        )
   
    

    st.markdown("<hr>", unsafe_allow_html=True)

    fig_mapa.update_layout(mapbox_style="open-street-map")
    fig_mapa.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

    # Aplica a margem com a div
    st.markdown('<div class="grafico-com-margem">', unsafe_allow_html=True)
    st.plotly_chart(fig_mapa, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)