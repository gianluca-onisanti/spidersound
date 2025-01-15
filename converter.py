import streamlit as st
import yt_dlp
import os
from pathlib import Path

def get_output_dir():
    # Retorna o diretório de downloads padrão do sistema operacional.
    if os.name == 'nt':  # Windows
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:  # Linux/macOS
        return str(Path.home() / "Downloads")

def download_audio(title):

    # Normalizar o título e buscar o vídeo no YouTube
    title = title.strip()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(get_output_dir(), '%(artist)s - %(title)s.%(ext)s'),
    }

    # Baixa o áudio do vídeo e remove o vídeo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"ytsearch:{title}", download=True)
        video = info_dict['entries'][0]

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
    if songs_text:
        # Processar a lista de músicas
        songs = songs_text.splitlines()
        i = 0
        for song in songs:
            download_audio(song)
            i+=1

        st.success(f"Música{'s' if i > 1 else ''} baixada{'s' if i > 1 else ''} na sua pasta > C://Downloads")
    else:
        st.warning("Por favor, insira a lista de músicas.")