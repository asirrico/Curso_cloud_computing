# Calcular area y volumen de cilindro
# Para el calculo que vamos a realizar debemos conocer el radio y la altura de dicho cilindro
# Estos dos datos se pedirán por teclado
import math
print("Introduzca la longitud del radio del cilindro en cm: ")
r=float(input())
print("Introduzca la altura del radio del cilindro en cm: ")
h=float(input())

area=2*math.pi*(r+h)
volumen=math.pi*r**2*h

print(f"El área del cilindro es {area} cm² y el volumen es {volumen} cm³")