###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte 
###

# Asignar una variable
# solo hace falta poner esto
my_name = "garsovia"
# print(my_name)

age = 29
# print(age)

# age = 39
# print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# que no tienes que declararlo explícitamente
# my_name = "garsovia"
# print(type(my_name))

# name = 29
# print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automáticas
# print(10 + "2)

# f-string (literal de cadena de formato)
# desde la versión Python 3.6
print(f"Hola {my_name}, tienes {age + 5} años")

# No recomendad forma de asignar variables
name, age, city = "garsovia", 29, "Sevilla"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

MiNombreDeVariable = "ko"  # PascalCase
minombredevariable = "ko" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE --> constantes (se usa para valores que no cambian, pero que pueden ser reasignados)


# Nombres no válidos de variables
# 123_mi_variable = "ko" # no puede empezar por número
# mi-variable = "ko" # no puede contener guiones
# mi variable = "ko" # no puede contener espacios

# True = False # no puede usar palabras reservadas

# ['False', 'None', 'True', 'and', 'as', 'assert', 
# 'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally', 
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield'] 

is_user_logged_in : bool = True
print(is_user_logged_in)

