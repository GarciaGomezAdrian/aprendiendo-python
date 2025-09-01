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