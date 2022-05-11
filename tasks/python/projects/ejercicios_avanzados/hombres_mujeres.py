import enum
import random


class Persona:
    id_persona=None
    nombre=None
    apellidos=None
    edad=None
    sexo=None
    nacionalidad=None
    def __init__(self,id_persona,nombre,apellidos,edad,sexo,nacionalidad):
        self.id_persona=id_persona
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.sexo=sexo
        self.nacionalidad=nacionalidad
        
    def print_nombre(self):
        return self.id_persona
        
#Declaramos dos arrays de nombres y uno de apellidos

nombres_hombre=["Juan Antonio","Manuel","Billy","Sergio","Víctor","Marco","Carlos","Alfonso","Jose","Alex"]
nombres_mujer=["Beatriz","María","Guadalupe","Andrea","Lucía","Carmen","Belén","Marta","Alex","Vanesa"]
apellidos=["Sánchez","García","Blanco","Lapaz","Romero","Cejudo","Algar","Reyes","Suarez"]


#Ahora declaramos los arrays donde almacenaremos las personas por sexo y otro array donde alamacenaremos todas las personas
hombres=[]
mujeres=[]
personas=[]

p1=Persona(1,"juan","cejudo",22,"H","ESP")
print(p1.print_nombre())
hombres.append(p1)
print(hombres[0].nombre)
i=int(1)
while i < 100:
    p1=Persona(1,"Juan Antonio","Cejudo Algar",22,"H","ESP")
    i=1+i
    print(i)


