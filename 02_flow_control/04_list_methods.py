###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

lista1 = ['a', 'b', 'c', 'd',]

# Añadir o insertar elementos a la lista

lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posicion que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😀', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Elimina el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del lista[1:3]
print(lista)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort() # Ordena la lista de menor a mayor
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers) # Crea una nueva lista ordenada de menor a mayor
print(sorted_numbers)
print(numbers)

print('Ordenar una lista de cadenas de textos (todo minúscula)')
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print('Ordenar una lista de cadenas de textos (mezclas mayúscula y minúscula)')
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐶', '🐱']
print(len(animals)) # Tamaño de la lista -> 4
print(animals.count('🐶')) # Cuenta cuántas veces aparece el elemento '🐶' en la lista -> 2
print('🐼' in animals) # Comprueba si hay un panda '🐼' en la lista -> True
print('🐸' in animals) # Comprueba si hay una rana '🐸' en la lista -> False


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

print("\nEjercicio 1: Añadir y modificar elementos")
lista = [1, 2, 3, 4, 5]
print(f"Lista inicial: {lista}")
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(f"Lista modificada: {lista}")

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print("\nEjercicio 2: Combinar y limpiar listas")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
print(f"Lista_a: {lista_a}")
print(f"Lista_b: {lista_b}")
lista_a.extend(lista_b)
print(f"Comprobacion extend: {lista_a}")
lista_a.remove(1)
print(f"Comprobacion remove: {lista_a}")
eliminado_pop = lista_a.pop(3)
print(f"Imprimir el elemento eliminado: {eliminado_pop}")
lista_b.clear()
print(f"Comprobación del clear: {lista_b}")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\nEjercicio 3: Slicing y eliminación con del")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista inicial: {lista}")
del lista[2:5]
print(f"Lista resultante: {lista}")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print("\nEjercicio 4: Ordenar y contar")
numeros = [5, 2, 8, 1, 9, 4, 2]
print(f"Lista inicial: {numeros}")
numeros.sort()
print(f"Lista ordenada: {numeros}")
print(f"El número 2 aparece {numeros.count(2)} veces en la lista.")
print(f"¿El número 7 está en la lista?: {7 in numeros}")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print("\nEjercicio 5: Copia vs. Referencia")
original = [1, 2, 3]
print(f"Lista original: {original}")
copia_1 = original[:]
print(f"Copia 1 (slicing): {copia_1}")
copia_2 = original.copy()
print(f"Copia 2 (copy): {copia_2}")
referencia = original
referencia[0] = 10
print(f"Lista original (después de modificar referencia): {original}")
print(f"Copia 1 (después de modificar referencia): {copia_1}")
print(f"Copia 2 (después de modificar referencia): {copia_2}")
print(f"Referencia (modificada): {referencia}")

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: º.
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print("\nEjercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas")
frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)