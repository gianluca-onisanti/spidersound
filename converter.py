import streamlit as st
import time
from utils import *

st.set_page_config(page_title="SpiderSound - Extrator YT")

# Título da aplicação
st.markdown(
    """

        <style>
            .stButton>button {
                display: block;
                margin: 0 auto;
                width: 50%; /* Ajuste a largura conforme necessário */
            }
        </style>

        <h1 style='text-align: center;'>
            <span style='color: red;'>Spider</span>Sound
        </h1>

        <h3 style='text-align: center;'>
            Extrator de áudios do YouTube
        </h3>
    
    """, unsafe_allow_html=True)

# Área para inserir as músicas
songs_text = st.text_area("Digite o título das músicas (uma por linha):")

# Botão para iniciar o download
if st.button("Converter e Baixar"):
    placeholder = st.empty() 

    if songs_text:
        # Processar a lista de músicas
        songs = songs_text.splitlines()
        i = 0
        for song in songs:
            placeholder.info(f'Baixando: {song} . . .')
            download_audio(song)
            i+=1

        placeholder.success(f"{i} Música{'s' if i > 1 else ''} baixada{'s' if i > 1 else ''} com sucesso na pasta > C://Downloads")
        time.sleep(2.2)
        placeholder.empty()
    else:
        placeholder.warning("Por favor, insira a lista de músicas.")
        time.sleep(2.2)
        placeholder.empty()