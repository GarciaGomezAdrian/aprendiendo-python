# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

from os import system
if system("clear") != 0: system("cls")

# 1. Sin dependencias (difícil y sin dependencias)
import urllib.error
import urllib.request
import json


api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode('utf-8'))
  print(json_data)
  response.close()
except urllib.error.URLError as e:
  print(f"Error en la solicitud: {e}")


# 2. Con dependencia (requests)
import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
print(response.json())

# 3. Un POST
print("\nPOST:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
input = {
  "tittle": "Adrian",
  "body": "El mejor de todos los tiempos",
  "userId": 5
}
response = requests.post(api_posts, json=input)
print(response.json())

# Otra forma de hacer POST con todo incluido y mas pequeño
print("\nPOST simplificado:")
try:
  response = requests.post(
    "https://jsonplaceholder.typicode.com/posts/", 
    json={
      "tittle": "Adrian",
      "body": "El mejor de todos los tiempos",
      "userId": 5
    })
  print(response.json())
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")


# 4. Un PUT
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1", # Para poder modificarlo hay que ir directo al recurso, poner el id en la url
    json={
      "tittle": "Adrian",
      "body": "El mejor de todos los tiempos",
      "userId": 1
    })
  print(response.json())
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")


# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

print("\nGeneracion con API OPENAI:")
OPENAI_KEY = "sk-XXXXXXX"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])



# Llamar a la API de DEEPSEEK:
print("\nGeneracion con DEEPSEEK:")
DEEPSEEK_API_KEY = "sk-XXXXXXX"

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])