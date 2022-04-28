# ¡¡¡¡¡Si llamamos a este fichero datetime.py y ejecutamos, no funcionará. No podemos llamar a un fichero nuestro como a una librería que importamos.!!!!!
#Importamos datetime del modulo datetime
from datetime import datetime

#Importamos todo el módulo datetime
#import datetime

datenow1=datetime.now().date()
print("Fecha: ",datenow1)

datenow2=datetime.now()
print("Fecha: ",datenow2)
print("Año: ",datenow2.year)
print("Mes: ",datenow2.month)
print("Día: ",datenow2.day)
print(f"Hora:{datenow2.hour}",datenow2.hour)