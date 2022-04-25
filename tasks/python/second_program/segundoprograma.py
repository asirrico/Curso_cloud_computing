# Asignación simultánea

a=5
b=10
print ("Paso1. Valores iniciales")
print(a)
print(b)

temp=b
b=a
a=temp
del temp
print ("Paso2. Reasignamos valores ")
print(a)
print(b)