###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Solución ejercicio 1:

nombre = "Adrián"
ciudad = "Sevilla"

print(nombre)
print(ciudad)


print("--------------")


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Solución ejercicio 2:

print(f"Tipo de a: {type(a)}")
print(f"Tipo de b: {type(b)}")
print(f"Tipo de c: {type(c)}")
print(f"Tipo de d: {type(d)}")
print(f"Tipo de e: {type(e)}")


print("--------------")


print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Solución ejercicio 3:

cadena = "12345"
cadena_entero = int(cadena)
cadena_float = float(cadena_entero)

print(f"Numero entero: {cadena_entero}")
print(f"Numero como float: {cadena_float}")

cadena2 = 3.99
cadena2_entero = int(cadena2)

print(f"Float original: {cadena2}")
print(f"Float convertido a entero: {cadena2_entero}")


print("--------------")


print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Solución ejercicio 4:

nombre = "Adrián"
edad = 29
altura = 1.78

print(f"Hola! Mi nombre es {nombre}, tengo {edad} años y mido {altura} metros")


print("--------------")


print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Solución ejercicio 5:

resultado = int(round(3.1416) / 2)
print(f"Valor de PI (aproximado): {3.1416}")
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)
