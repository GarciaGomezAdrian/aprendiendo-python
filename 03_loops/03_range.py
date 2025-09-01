###
# 03 - range()
# Permiten crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

nums = range(5)

print("\nRango de 0 a 4:")
for num in nums:
  print(num)

# Generado una secuencia de números del 0 al 9
print("\nRango de 0 a 9:")
for num in range(10):
  print(num)

# range(inicio, fin)
print("\nRango de 5 a 9:")
for num in range(5, 10):
  print(num)

# range(inicio, fin, paso)
print("\nRango de 0 a 999 pasando de 5 en 5:")
for num in range(0, 1000, 5):
  print(num)

print("\nrange() con numeros negativos:")
for num in range(-5, 0):
  print(num)

print("\nEjemplo de cuenta atrás:")
for num in range(10, 0, -1):
  print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# range() para repetir acciones
for _ in range(5):
  print("Hacer cinco veces algo")


###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for num in range(1, 11):
  print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for impar in range(1, 21):
  if impar % 2 != 0:
    print(impar)

print("\nEjercicio 2 (Otra forma de hacerlo):")
for impar in range(1, 21, 2):
  print(impar)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for multiplo in range(5, 51, 5):
  print(multiplo)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for numero in range(10, 0, -1):
  print(numero)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for num in range(1, 101):
  suma += num
print(f"La suma de los numeros del 1 al 100 (inclusive) es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un número para la tabla de multiplicar: "))
for num in range(1, 11):
  print(f"{numero} x {num} = {numero * num}")