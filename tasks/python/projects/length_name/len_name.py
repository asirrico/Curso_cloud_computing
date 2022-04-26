### Calcular longitud de un nombre y especificar posición de cada letra

print("Introduzca un nombre:")
nombre=input()

longitud=len(nombre)
print("La longitud del nombre introducido es: " + str(longitud))


for i in range(0,longitud):
    print("La posición " + str(i) + " corresponde con la letra " + nombre[i])