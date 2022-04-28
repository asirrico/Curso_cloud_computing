### Calcular longitud de un nombre y especificar posición de cada letra

print("Introduzca un nombre:")
nombre=str(input())

### Calculamos la longitud del nombre
longitud=len(nombre)
print("La longitud del nombre introducido es: " + str(longitud))

### Mostramos los carácteres que forman el nombre y su posición

for i in range(0,longitud):
    print("La posición " + str(i) + " corresponde con la letra " + nombre[i])