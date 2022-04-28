# A partir de un número ingresado, decir si es mayor, menor o igual a 9

print("Escribir número: ")
x=input()

if (x.isdigit()):

    x=int(x)
    if (x==9):
        print(str(x) + " es igual a 9")
    elif (x>9):
        print(str(x) + " es mayor que 9")
    else:
        print(str(x) + " es menor que 9")
else:
    print("No ha introducido un número")