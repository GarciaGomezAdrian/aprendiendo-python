# Trabajando con fechas y horas en Python

from os import system
if system("clear") != 0: system("cls")

from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora específica
specific_date = datetime(2025, 2, 25, 15, 30, 0)
print(f"Fecha y hora específica: {specific_date}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato: 
format_date = now.strftime("%d/%m/%Y %H:%M:%S") # Las / hay que añadirla para que aparezca, igual si quieres separar por guiones - 
print(f"Fecha formateada: {format_date}")       # o por cualquier separador que quieras

format_date = now.strftime("%A, a %d de %B de %Y").capitalize() # capitalize() se usa para poner la primera en mayúscula
print(f"Fecha formateada: {format_date}")

# 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

yesterday = datetime.now() - timedelta(days=0.5)
print(f"Ayer: {yesterday}")

# 5. Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6. Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 25, 15, 30, 0)
difference_date = date2 - date1
print(f"Diferencia entre las fechas: {difference_date}")

