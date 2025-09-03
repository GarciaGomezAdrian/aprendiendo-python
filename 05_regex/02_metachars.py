###
# 02 - Meta caracteres
# Los metacaracteres son símbolos especiales con significados específicos en las expresiones regulares
###

from os import system
if system("clear") != 0: system("cls")

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva línea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------------------

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r"\d", text)

print(found)

# \d{nª} para que coincida con la longuitud del número
text = "El número de teléfono es 123456789"
found = re.findall(r"\d{9}", text)

print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono: {found.group()}")


# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, o-9, _)
text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)


# \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás\t?"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)


# ^: Coincide con el principio de una cadena
text = "%423_name"
pattern = r"^\w" # validar nombre de usuario
valid = re.search(pattern, text)

if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} "
valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "Hola Mundo"
pattern = r"mundo$"
valid = re.search(pattern, text, re.IGNORECASE)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# Ejercicio:
# Valida que un correo sea de gmail
text = "adrian@gmail.com"
pattern = r"^\w+@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail válido")
else: print("El correo no es válido")

# Ejercicio:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extensión .txt
files = "file.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.+txt\b"
matches = re.findall(pattern, files)

print(matches)

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bcasa\b"
found = re.findall(pattern, text)
print(found)

# |: Coincidir con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"
found = re.findall(pattern, fruits)

print(found)