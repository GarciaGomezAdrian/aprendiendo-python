print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()
contador = 0
for palabra in palabras:
  if palabra.lower().startswith(letra):
    contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")