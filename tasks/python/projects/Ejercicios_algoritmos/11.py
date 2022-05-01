from operator import truediv


print("Escribir un número: ")
nro = int(input())
div = int(2)
band=True
if (nro==int(1)):
    print(f"El número introducido ({nro}) es primo")
else:
    while (band==True & nro>div):
        if(int(nro%div)==int(0)):
            band=False
    div+=1  

if (band==True):
    print("Es primo")
else:
    print("No es primo")