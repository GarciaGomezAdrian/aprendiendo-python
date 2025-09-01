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