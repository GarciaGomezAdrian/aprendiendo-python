###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
###

from os import system
if system("clear") != 0: system("cls")

print("\nBucle while:")

# Bucle con una simple condición
contador = 0
while contador <= 5:
  print(contador)
  contador += 1 # Es super importante para evitar un bucle infinito


print("\nBucle while con break:")
# Utilizando la palabra break, para romper el bucle
contador = 0
while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # Sale del bucle

contador = 0
while contador <= 100:
  print(contador)
  contador += 1
  if contador % 5 == 0:
    print(contador)
    print("El numero es múltiplo de 5")
    break

# continue, lo que hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\nBucle con continue:")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0: # si esto es true vuelve a reiniciar el while sin pasar
    continue            # por el print(contador)

  print(contador)

# else, esta condición cuando se ejecuta?
print("\nBucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# Pedirle al usuario un número que tiene que ser positivo, si no, no lo dejamos en paz
numero = -1
while numero <= 0:
  numero = int(input("Escribe un número positivo: "))
  if numero <= 0:
    print("El número debe ser positivo. Intenta otra vez maj@.")

print(f"El número que has introducido es {numero}")



numero = -1
while numero <= 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero <= 0:
      print("El número debe ser positivo. Intenta otra vez maj@.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 10
while contador >= 1:
  print(contador)
  contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 1
resultado = 0
while contador <= 20:
  if contador % 2 == 0:
    resultado += contador
  contador += 1
print(f"La suma de los números pares entre 1 y 20 es: {resultado}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

usuario = int(input("Introduce un número entero positivo: "))
resultado = 1
while usuario > 0:
  resultado *= usuario
  usuario -= 1
print(f"El factorial del numero introducido por el usuario es: {resultado}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contraseña = ""
while len(contraseña) < 8:
  contraseña = input("Introduce una contraseña (al menos 8 caracteres): ")
  if len(contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtelo de nuevo.")
print("Contraseña válida!!")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

usuario = int(input("Introduce un número para hacer su tabla de multiplicar: "))
print(f"\nLa tabla multiplicar del número {usuario} es:")
multiplicador = 1
while multiplicador <= 10:
  print(f"{usuario} x {multiplicador} = {usuario * multiplicador}")
  multiplicador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1