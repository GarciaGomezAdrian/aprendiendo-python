###
# 04 - sets
###

from os import system
if system("clear") != 0: system("cls")

import re

# []: Coincide con cualquier carácter dentro de los corchetes
username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match: print("El nombre de usuario es válido: ", match.group())
else: print("El nombre de usuario no es válido")


# Ejercicio: Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontra las palabras man, fan y ban pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)


# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana fan fanfarron"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
text = "lo.que+sea@shopping.online"
pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z.]{2,6}"

validate = re.search(pattern, text)

if validate: print("El correo es válido ", validate.group())
else: print("El correo es inválido")


text = "michael@gov.co.uk"
pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z.]{2,6}"

validate = re.search(pattern, text)

if validate: print("El correo es válido ", validate.group())
else: print("El correo es inválido")

# [^]: Coincide con cualquier carácter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)