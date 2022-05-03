numero = input("Introduzca un número: ")
if (numero.isdigit()):

    numero = int(numero)
    resultado = 0
    while numero != 0:
        resultado = resultado + (numero % 10) 
        numero = numero//10
    print(f"El resultado es {resultado}")
else:
    print("Introduzca un número válido")