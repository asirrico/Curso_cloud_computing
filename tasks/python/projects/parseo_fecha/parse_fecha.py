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

#Fecha en formato americano
#Capturamos la fecha actual
fecha3=datetime.now()
print("Fecha 3: ", fecha3)
#Imprimimos la fecha en formato americano
print("Fecha 3: ",fecha3.strftime("%A %d %b %Y"))

#Proceso de pasar fecha a español
#Importamos libreria locale para poder transformar a castellano
# Si da fallo hacer : python3 -c "import locale; locale.setlocale(locale.LC_ALL, '')"
import locale
 

locale.setlocale(locale.LC_TIME, 'es_ES.UTF8') 

fechacastellano = datetime.now()
print("Fecha en castellano: ",fechacastellano.strftime("%A %d %b %Y"))
