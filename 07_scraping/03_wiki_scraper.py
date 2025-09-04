from bs4 import BeautifulSoup
import requests

url = "https://es.wikipedia.org/wiki/Web_scraping"
headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0.0 Safari/537.36"
          }

response = requests.get(url, headers=headers)

if response.status_code == 200:
  print("Peticion correcta")

  soup = BeautifulSoup(response.text, "html.parser")

  # Extraer todos los titulos <h1>
  titulos = [titulo.string for titulo in soup.fin_all("h1")]
  print(titulos)

  # Extraer todos los enlaces <a>
