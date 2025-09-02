###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados
###

from os import system
if system("clear") != 0: system("cls")

# Ejemplo típico de diccionario
persona = {
  "nombre": "Adrian",
  "edad": 29,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "social": {
    "twitter": "@Garsovia",
    "instagram": "Garsovia",
    "facebook": "Garsovia"
  }
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["social"]["twitter"])

# Cambiar valores al acceder o añadirlos en el caso de que no existan
persona["nombre"] = "Adrian Garcia"
persona["calificaciones"][2] = 10

# Eliminar completamente una propiedad
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# Sobreescribir un diccionario con otro diccionario
a = { "name": "Paula", "age": 27 }
b = { "name": "Lucia", "es_estudiante": True }

b.update(a)
print(b)

# Comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# Obtener todas las claves
print("\nkeys:")
print(persona.keys())

# Obtener todos los valores
print("\nvalues:")
print(persona.values())

# Obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
  print(f"{key}: {value}")