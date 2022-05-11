
# Adivinar la palabra
# El siguiente programa va a tratar de descubrir la palabra que le hemos introducido
# Vamos a realizar fuerza bruta a cada carácter de la palabra hasta conseguir descifrarla

palabra="Palabra muy secreta ½ con una fracción &"
l=len(palabra)
descifrada=str()
abecedario=" aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ0123456789áéíóú.:,;!·$%&/()=?¿|@#~½¬{[]}\][{─·-̣ºª<>\\"
for i in range(0,l):
    for r in range(0,108):
        letra=abecedario[r]
        if(letra==palabra[i]):
            descifrada=descifrada+letra
            break

print(descifrada)



