# pip3 install requests -> instaladas las dependencias para hacer peticiones

import requests
import re

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
  print("Peticion correcta")

  html = response.text
  # print(html)
  # Podriamos hacer una regulara expresion para encontrar el precio
  price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
  match = re.search(price_pattern, html)

  if match:
    print(f"El precio del producto es: {match.group(1)}")

  # get the title if the pattern is found
  title_pattern = r'<title>(.*?)</title>'
  match = re.search(title_pattern, html)

  if match:
    print(f"El titulo de la web es: {match.group(1)}")
