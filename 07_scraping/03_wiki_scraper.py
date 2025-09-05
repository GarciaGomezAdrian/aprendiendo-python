from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scrape_url(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Peticion correcta")

        soup = BeautifulSoup(response.text, "html.parser")

        # Extraer todos los titulos <h1>
        # titulos = [titulo.string for titulo in soup.find_all("h1")]
        # print(titulos)

        # Extraer todos los enlaces <a>
        # enlaces = [urljoin(url, enlace.get("href")) for enlace in soup.find_all("a")]
        # print(enlaces)

        # Extraer todo el contenido de la página de texto
        # all_text = soup.get_text()
        # print(all_text)

        # Extraer el texto del elemento main
        # main_text = soup.find('main').get_text()
        # print(main_text)

        # Extraer de la id mw-content-text
        # content_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
        # print(content_text)

        # Extraer el open graph si existe
        # og_image = soup.find('meta', {'property': 'og:image'})
        # if og_image:
        #     print(og_image['content'])
        # else:
        #     print("No se ha encontrado la imagen")

        og_image = soup.find('meta', property='og:image')
        if og_image:
            print(og_image['content'])
        else:
            print("No se ha encontrado la imagen")

scrape_url("https://midu.dev")
# scrape_url("https://es.wikipedia.org/wiki/Web_scraping")
