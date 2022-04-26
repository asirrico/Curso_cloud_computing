
###Vamos a concatenar de manera eficiente

#Declaramos variables
saludo="Hola "
nombre="Juan Antonio"
ciudad="Madrid"

#Concatenamos de manera eficiente
## Esta manera de concatenar consigue unir texto si generar espacios adicionales de memoria interna
print("{a}{b} bienvenido a {c}".format(a=saludo,b=nombre,c=ciudad))

#Concatenación no eficiente
## Esta concatenación crea un espacio de memoria donde une todo el texto, en vez de aprovechar las ya existentes.
## A la larga esta concatenación es menos eficiente
print(saludo + nombre + " bienvenido a " + ciudad)
