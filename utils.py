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
