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
