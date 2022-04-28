# Comprobación paridad número ingresado

while (True):

    print("Ingrese un número: ")
    n=input()
    if(n.isdigit()):
        
        n=int(n)
        if(n%2==0):
            print(str(n) + " es par.")
            break
            
        else: 
            print(str(f))
            print(str(n) + " es impar.")
            break
            
    else:
        print("No ha ingresado un número")

