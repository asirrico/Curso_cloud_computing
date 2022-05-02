# Adivinar la palabra
# El siguiente programa va a tratar de descubrir la palabra que le hemos introducido
# Vamos a realizar fuerza bruta a cada carácter de la palabra hasta conseguir descifrarla

palabra="cba"
l=len(palabra)
v=[l]
descifrada="abc"
abecedario=["a","b","c"]
for i in range(1,l+1):
    contador=0
    for r in range(0,2):
        letra=abecedario[r]
        if(letra==palabra[i]):
            descifrada[contador]=letra
print(descifrada)
