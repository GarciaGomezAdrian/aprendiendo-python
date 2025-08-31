###
# 03 - Listas
# Secuencias mutables de elementos. 
# Pueden contener elementos de diferentes tipos.
###

from encodings import palmos
import os
os.system("clear")

# Creación de listas
print ("\nCrear listas")

lista1 = [1, 2, 3, 4, 5] # listas de enteros
lista2 = ["manzana", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ["calcetín", 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
print("\nSlicing (rebanado) de listas")
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])  # [2, 3, 4]
print(lista1[:3])   # [1, 2, 3]
print(lista1[3:])   # [4, 5]
print(lista1[:])    # [1, 2, 3, 4, 5]

# HAY MAS MAGIA
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares [1, 3, 5, 7]
print(lista1[::-1]) # para devolver la lista al revés

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a la lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista:", len(lista1))



###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\nEjercicio 1: El mensaje secreto")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print(secreto)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\nEjercicio 2: Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\nEjercicio 3: El sándwich de listas")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\nEjercicio 4: Duplicando la lista")
lista = [1, 2, 3]
lista_dupliacda = lista + lista
print(lista_dupliacda)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\nEjercicio 5: Extrayendo el centro")
lista = [10, 20, 30, 40, 50]
print(lista[2:3])

print("\n(OTRA POSIBILIDAD) Ejercicio 5: Extrayendo el centro")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("\nEjercicio 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
mitad = lista[:3]
nueva_lista = mitad[::-1] + lista[3:]
print(nueva_lista)

print("\n(OTRA POSIBILIDAD) Ejercicio 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)