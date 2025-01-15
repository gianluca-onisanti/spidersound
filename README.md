# SpiderSound

SpiderSound é um aplicativo em Python que utiliza Streamlit para criar uma interface web simples e yt_dlp para baixar vídeos do YouTube no formato WEBM.

## Ferramentas Utilizadas

- **Streamlit v1.38.0**
- **yt_dlp v2025.1.12**

## Como Usar

1. Certifique-se de que todos os pacotes necessários estão instalados. Você pode instalar os pacotes listados em `requirements.txt` com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```
2. Navegue até a pasta onde está o projeto. Ex:
    ```bash
    cd /c:/sua/pasta/do/projeto/spidersound
    ```
3. Execute o aplicativo com o comando:
    ```bash
    streamlit run converter.py
    ```

4. Você será redirecionado a seu navegador para a página do SpiderSound. Digite os títulos dos vídeos que deseja baixar (1 por linha).

5. Clique em **"Converter e Baixar"**.

6. Pronto! Seus arquivos de áudoio estarão em sua pasta Downloads.
