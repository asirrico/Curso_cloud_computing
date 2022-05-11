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
        
#Declaramos dos arrays de nombres, uno de apellidos y uno de nacionalidades.
nombres_hombre=["Juan Antonio","Manuel","Billy","Sergio","Víctor","Marco","Carlos","Alfonso","Jose","Alex"]
nombres_mujer=["Beatriz","María","Guadalupe","Andrea","Lucía","Carmen","Belén","Marta","Alex","Vanesa"]
apellidos=["Sánchez","García","Blanco","Lapaz","Romero","Cejudo","Algar","Reyes","Suarez","López"]
nacionalidades=["ESP","FR","MC","US","GB","ITA","CH","MX"]

hombres=[]
mujeres=[]
personas=[]

#Aquí declaramos un objeto de clase persona, iremos modificando los atributos en cada una de las iteraciones del bucle que vamos a crear a continuación

p1=Persona("","","","","","")


#Aquí creo 3 contadores, uno es "i" actúa como flag para controlar el bucle, los otros dos sirven para contar el número de hombres y mujeres que hemos generado
i=1
male_count=0
female_count=0
#Añado contadores adicionales a los que ya tenía el ejercicio anterior, "count_uppper18" nos servirá para almacenar la cuenta de personas mayores de 18 años.
count_upper18=0
count_lower=0
#flag_misma_edad_mayor=0
#flag_misma_edad_menor=0
#nombre_mayor=""
#posicion_mayor=int()
#nombre_menor=""
#posicion_menor=int()


while i < 101:
    sexo=random.randint(1,2)
    if (sexo==1):
        female_count=female_count+1
        sexo="F"
        p1.nombre=str(nombres_mujer[random.randint(0,9)])
        p1.apellidos=str(apellidos[random.randint(0,9)]+" "+apellidos[random.randint(0,9)])
        p1.edad=random.randint(1,120)
        p1.sexo=sexo
        p1.nacionalidad=nacionalidades[random.randint(0,7)]
        personas.append(p1)
#        print(f"{p1.nombre} {p1.apellidos} {p1.edad} {p1.nacionalidad} {p1.sexo}")
        i=i+1


    else:
        male_count=male_count+1
        sexo="M"
        p1.nombre=str(nombres_hombre[random.randint(0,9)])
        p1.apellidos=str(apellidos[random.randint(0,9)]+" "+apellidos[random.randint(0,9)])
        p1.edad=random.randint(1,120)
        p1.sexo=sexo
        p1.nacionalidad=nacionalidades[random.randint(0,7)]
        personas.append(p1)
#        print(f"{p1.nombre} {p1.apellidos} {p1.edad} {p1.nacionalidad} {p1.sexo}")
        i=i+1
    
    if (p1.edad>=18):
        count_upper18=count_upper18+1



#print(f"{personas[20].nombre} {personas[20].apellidos} {personas[20].edad} {personas[20].nacionalidad} {personas[20].sexo}  ")

print(f"El porcentaje de hombres es de {male_count}%")
print(f"El porcentaje de mujeres es de {female_count}%")
print(f"En total tenemos {female_count+male_count} personas")
print(f"Hay un total de {count_upper18} personas mayores de 18 años")

#dict(zip(range(len(personas)), personas))
