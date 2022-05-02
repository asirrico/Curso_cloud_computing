# Calcular factorial de un número introducido por teclado

print("Introduzca un número")
x=int(input())
factorial=1

if(x<0):
    print("Error, no existe factorial para número negativo")
elif(x==0):
    print("El factorial de 0 es 1")
else:
    for i in range(1,x+1):
        factorial = factorial * i


    print(f"El factorial de {x} es {factorial}")