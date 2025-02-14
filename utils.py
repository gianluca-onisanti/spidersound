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

def download_audio(input_data):
    """
    Baixa o áudio de um vídeo do YouTube.

    Args:
        input_data:  Pode ser o título do vídeo (string) ou a URL do vídeo (string).
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(get_output_dir(), '%(artist)s - %(title)s.%(ext)s'),
        'noplaylist': True,  # Importante: Evita baixar playlists inteiras se a URL for de uma playlist.
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if input_data.startswith('http'):  # É uma URL
            try:
                info_dict = ydl.extract_info(input_data, download=False)  # Extrai informações SEM baixar
                title = info_dict.get('title', None) #Pega o título
                
                if not title:
                   raise ValueError("Não foi possível obter o título do vídeo a partir da URL.")
                
                print(f"Título obtido da URL: {title}")
                #Agora faz o download usando as opções e o título extraído
                info_dict = ydl.extract_info(input_data, download=True)


            except yt_dlp.utils.DownloadError as e:
                 if "is not a valid URL" in str(e):
                    raise ValueError("URL inválida.") from e  # Lança um erro mais específico
                 else:
                     raise  # Re-lança outros erros do yt-dlp

        else:  # É um título (string)
            title = input_data.strip()
            info_dict = ydl.extract_info(f"ytsearch:{title}", download=True)
            if not info_dict['entries']:
                raise ValueError(f"Nenhum vídeo encontrado para o título: '{title}'")
            video = info_dict['entries'][0]