###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

from os import system
if system("clear") != 0: system("cls")

import re

# *: Puede aparecer 0 o mas veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

palabras = "palabra, colabora, peligro, calor, sofocaba, marcador, carbon, aburrido"
pattern = r"\w+a*b\w+"
matches = re.findall(pattern, palabras)
print(matches)

# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = r"a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = r"a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+?34 \d{9}"
valid = re.findall(pattern, phone)
print(valid)

# {n}: Exactamente n veces
text = "aaaaaa"
pattern = r"a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m}: de n a m veces
text = "u uu uuu uuuu u"
pattern = r"u{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Encuentra las palabras de 4 a 6 letras
words = "ala casa árbol león cinco murciélago"
pattern = r"\b\w{4,6}\b"
found = re.findall(pattern, words)
print(found)

# Ejercicio: Encuentra las palabras de mas de 6 letras
words = "ala fantástico casa árbol león cinco murciélago"
pattern = r"\b\w{6,}\b"
found = re.findall(pattern, words)
print(found)