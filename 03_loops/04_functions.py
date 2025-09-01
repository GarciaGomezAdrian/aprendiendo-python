###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas específicas
###

from os import system
if system("clear") != 0: system("cls")

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
  # docstring
  # cuerpo de la función
  return valor_de_retorno # opcional
"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
  print("Hola!")

saludar()

# Ejemplo de una función con parámetros
def saludar_a(nombre):
  print(f"Hola {nombre}")

saludar_a("Adrián")
saludar_a("Ana")
saludar_a("Paula")

# Funciones con mas parámetro
def sumar(a, b):
  suma = a + b
  return suma

result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
  """Resta dos números y devuelve el resultado"""
  return a - b

print(restar.__doc__)
# help(restar) # Muy bueno si queremos ver esta funcion

# Parámetros por defecto
def multiplicar(a, b = 2):
  return a * b

print(multiplicar(2))
print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre, edad, sexo):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# Parámetro son posicionales
describir_persona("Adrián", 29, "macho alfa")
describir_persona("Adrián", "macho alfa", "29")

# Argumentos por clave
# Parámetros nombrados
describir_persona(sexo="macho alfa", nombre="Adrián", edad=29)
describir_persona(sexo="jefa suprema", nombre="Paula", edad=27)

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Adrián", edad=29, sexo="hombre")
print("\n")
mostrar_informacion_de(name="Paula", edad=27, country="España")
print("\n")
mostrar_informacion_de(nick="Garsovia", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="Alonsito", es_mod=True, gatos=4)