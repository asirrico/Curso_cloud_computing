# Adivinar la palabra
# El siguiente programa va a tratar de descubrir la palabra que le hemos introducido
# Vamos a realizar fuerza bruta a cada carácter de la palabra hasta conseguir descifrarla

from ntpath import join


palabra="cba"
l=len(palabra)
v=[l]
abecedario="abc"
for i in range(0,l):
    contador=0
    for r in range(0,l):
        letra=abecedario[r]
        if(letra==palabra[i]):
            descifrada=join(letra)
            contador=+1

print(descifrada)
