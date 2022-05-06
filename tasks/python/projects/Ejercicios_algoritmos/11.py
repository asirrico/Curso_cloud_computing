#Calcular si un número es primo
#Partiendo de la premisa de que un número primo es todo aquel número que solo es divisible por el mismo y por la unidad
#Dado un número introducido por teclado el programa debe decir si es o no primo
#Según la fuente el número 1 se puede o no tomar como número primo, debido a que solo tiene un divisor posible y es él mismo.
# En nuestro caso lo tomaremos como número primo

print("Introduzca un número")

try:
    e=int(input())
except:
    print("Error, no se ha introducido un número")
else:
    print("Realizando calculos")



#Creamos una flag
f=0

for i in range(2,e):
    if (e%i==0):
        f=1
        break
    
if (f==0):
    print(f"{e} es un número primo")
else:
    print(f"{e} no es un número primo")




