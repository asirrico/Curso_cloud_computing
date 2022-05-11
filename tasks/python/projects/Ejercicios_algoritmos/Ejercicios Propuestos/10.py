# Adivinar la palabra
# El siguiente programa va a tratar de descubrir la palabra que le hemos introducido
# Vamos a realizar fuerza bruta a cada carácter de la palabra hasta conseguir descifrarla



palabra="palabra muy secreta"
l=len(palabra)
descifrada=str()
abecedario=" aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ"
for i in range(0,l):
    for r in range(0,55):
        letra=abecedario[r]
        if(letra==palabra[i]):
            descifrada=descifrada+letra
            print(descifrada)
