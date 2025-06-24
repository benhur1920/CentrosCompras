import streamlit as st
import os



def exibir_sobre(totalLinhas):

    # caminho do arquivo imagem
    imagem_path3 = os.path.join(os.path.dirname(__file__), '..', 'images', 'mercadosaojose.jpg')  # ou o nome 
    
    col1, col2 = st.columns([3,4])  # proporção da largura das colunas

    with col1:
        st.image(imagem_path3, use_container_width=True,clamp=True, caption='Mercado de São José - Recife')  # define o tamanho da imagem em pixels
    with col2:
        
        st.markdown(
        f"""
        <div style="text-align: center;   margin-top: 10px">
        <h2>Principais centros de compras do Recife</h2>
            <p style="font-size: 20px;">
            Aqui você vai encontrar cerca de <strong>{totalLinhas} </strong> dos principais centros comerciais do Recife, com informações atualizadas e baseadas nos dados abertos disponibilizados pela Prefeitura.  
            Nossa plataforma é responsiva, ou seja, funciona bem no celular, tablet ou computador, para você acessar de onde estiver, na hora que precisar. Se estiver passeando pela cidade, querendo comprar algo ou planejar uma visita, já pode ter todas as informações na palma da mão, facilitando sua escolha e organização.  Você pode explorar os dados por bairro, região ou tipo de comércio, com gráficos interativos que deixam tudo mais fácil de entender. E se quiser, ainda pode baixar os dados para usar do jeito que preferir, seja para pesquisa, análise ou qualquer outro projeto.  Tudo pensado para deixar as informações comerciais do Recife acessíveis, práticas e na mão de todo mundo.
            </p>
            
        </div>
        """, unsafe_allow_html=True
    ) 
        
        

def mainSobre(totalLinhas):
    st.markdown("<hr style='border:2px'>", unsafe_allow_html=True)
    exibir_sobre(totalLinhas)
