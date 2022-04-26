#Importamos módulo necesario para trabajar con fechas
from datetime import datetime

#Ejemplo de capturar solo fecha
fecha="01-25-2000"
obj=datetime.strptime(fecha,'%m-%d-%Y').date()

print("La variable obj es de tipo " + str(type(obj)))

print(f"{obj.day}-{obj.month}-{obj.year}")

#Ejemplo de capturar fecha y hora, nos muestra solo la fecha porque arriba no introducimos fecha.

fecha2="01-25-2000"
obj=datetime.strptime(fecha,'%m-%d-%Y')

print("La variable obj es de tipo " + str(type(obj)))

print(f"{obj.day}-{obj.month}-{obj.year}")

