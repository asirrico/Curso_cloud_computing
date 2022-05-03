# Creación de una calculadora
def suma(x,y):
    z=x+y 
    print(f"El resultado de sumar {str(x)} y {str(y)} es: {str(z)}")

def resta(x,y):
    z=x-y
    print(f"El resultado de restar  {str(x)} y {str(y)} es: {str(z)}")

def producto(x,y):
    z=x*y
    print(f"El resultado de multiplicar {str(x)} por {str(y)} es: {str(z)}")

def fraccion(x,y):
    z=x/y
    print(f"El resultado de dividir {str(x)} entre {str(y)} es: {str(z)}")
i=0
while (i==0):
    print("¿Que operación realizo 0.Suma, 1.Resta, 2.Multiplicación o 3.División? Introducir número!!!")
    e = int(input())
    print("¿Que valor asignamos a numéro 1? Introducir número!!!")
    x = int(input())
    print("¿Que valor asignamos a numéro 2? Introducir número!!!")
    y = int(input())

    if(e==0):
        suma(x,y)
    elif(e==1):
        resta(x,y)
    elif(e==2):
        producto(x,y)
    elif(e==3):
        fraccion(x,y)
    else:
        print("Número introducido no corresponde con ninguna operación")   

    e = 3

    while (e!=0 and e!=1):
        print("Desea seguir realizando operaciones 1.Si 0.No")
        e=int(input())
        if (e==1):
            i=0
        elif(e==0):
            i=1
        else:
            print("Valor introducido erroneo")