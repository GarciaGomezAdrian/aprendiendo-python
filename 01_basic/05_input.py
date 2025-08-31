###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola
###

# print("Hola, ¿cómo te llamas?")
nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuántos años tienes?\n")
# print(f"Dentro de 20 años tendras {age + 20} años") # No se puede sumar un entero a una cadena ya que el input() devuelve un string
age = int(age)
print(f"Tienes {age} años")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué pais y ciudad vives?\n").split(", ")

print(f"Vives en {city}, {country}")

print(f"Hola soy {nombre} y tengo {age} años y vivo en {city}, {country}")
