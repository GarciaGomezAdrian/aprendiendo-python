from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
    print("Peticion correcta")

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())
    title_tag = soup.title
    if title_tag:
        print(f"El titulo de la web es: {title_tag.text}")

    # find price using bs
    price_span = soup.find("span", class_="rc-prices-fullprice")
    if price_span:
        print(f"El precio del producto es: {price_span.text}")


    # find all the prices
    prices_span_all = soup.find_all(class_="rc-prices-fullprice")
    for price in prices_span_all:
        print(f"El precio del producto es: {price.text}")

    # find each product and get the name and the price
    products = soup.find_all(class_="rc-productselection-item")
    for product in products:
        name = product.find(class_="list-title").text
        price = product.find(class_="rc-prices-fullprice").text
        print(f"El producto con las características: {name}\nPrecio de {price}\n\n")


