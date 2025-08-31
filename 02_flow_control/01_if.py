###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\n Sentencia condicional con else")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")

nota = 7
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("¡Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡Suspenso!")


print("\n Condiciones múltiples")

edad = 17
tiene_carnet = False

# Un pueblo de Valencia
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔")

# Un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
  print("A trabajar!")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
  if tiene_dinero:
    print("Puedes salir de fiesta 🎉")
  else:
    print("Quédate en casa")
else:
  print("No puedes salir de fiesta")

# Mas fácil:
# if edad < 18:
#  print("No puedes salir de fiesta")
# elif tiene_dinero:
#   print("Puedes salir de fiesta 🎉")
# else:
#   print("Quédate en casa")

numero = 5
if numero:
  print("El número no es cero")

numero = 0
if numero:
  print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
  print("El nombre no está vacío")

nombre = ""
if nombre:
  print("Aquí no entrará nunca")
else:
  print("El nombre está vacío")

numero = 3 # Asignación
es_el_tres = numero == 3 # Comparación

if es_el_tres:
  print("El número es 3")


print("\nLa condición ternaria:")
# Es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condición] else [código si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\n Ejercicio 1: Determinar el mayor de dos números")

mayor_uno = input("Introduce el primer número:\n")
mayor_dos = input("Introduce el segundo número:\n")

if int(mayor_uno) == int(mayor_dos):
  print("Los números son iguales")
elif int(mayor_uno) > int(mayor_dos):
  print(f"El número {mayor_uno} es mayor que {mayor_dos}")
else:
  print(f"El número {mayor_dos} es mayor que {mayor_uno}")



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\n Ejercicio 2: Calculadora simple")

calculadora_uno = float(input("Introduce el primer número: "))
calculadora_dos = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
  resultado = calculadora_uno + calculadora_dos
elif operacion == "-":
  resultado = calculadora_uno - calculadora_dos
elif operacion == "*":
  resultado = calculadora_uno * calculadora_dos
elif operacion == "/":
  if calculadora_dos == 0:
    print("Error: División por cero no permitida")
  else:
    resultado = calculadora_uno / calculadora_dos
else:
  print("Operación no válida")


if 'resultado' in locals(): # Comprueba si la variable resultado existe.
  print(f"El resultado es: {resultado}")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\n Ejercicio 3: Año bisiesto")
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
  print(f"{anio} es un año bisiesto")
else:
  print(f"{anio} no es un año bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\n Ejercicio 4: Categorizar edades")
edad = int(input("Introduce una edad: "))

if 0 <= edad <= 2:
  print("Bebé")
elif 3 <= edad <= 12:
  print("Niño")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= 65:
  print("Adulto mayor")
else:
  print("Edad no válida")

