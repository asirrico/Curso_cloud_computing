#Ingresar dos números y devolver la suma

n1=input("Introduzca número 1: ")
n2=input("Introduzca número 2: ")
resultado=0
if(n1.isdigit() & n2.isdigit()):
    n1=int(n1)
    n2=int(n2)
    resultado=n1+n2
    print(f"El resultado de sumar {str(n1)} y {str(n2)} es {str(resultado)}")
else:
    print("No ha introducido un número.")