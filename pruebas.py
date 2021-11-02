import os

def comparar(palabra, cadena):
    while palabra != cadena:
        letra= (input('Introduce una letra: ')).upper()
        cadena_t= " ".join(cadena)
        os.system("clear")
        for indice, valor in enumerate (palabra):
            if valor == letra:
                cadena[indice] = letra
                cadena_t= " ".join(cadena)
                os.system("clear")
                print(cadena_t)
            else:
                os.system("clear")
                print(cadena_t)
    os.system("clear")
    print("La palabra es "+str("".join(palabra))+", así que GANASTE, muchas felicidades!")
            
def run():
    palabra_random= list("LIBROO")
    os.system("clear")
    print('!Bienvenido al juego del ahorcado!')
    print('Adivina la palabra de '+ str(len(palabra_random)) + ' letras.')
    lineas = list(len(palabra_random)*"_")
    print(" ".join(lineas))
    print(comparar(palabra_random, lineas))

if __name__ == '__main__':
    run()