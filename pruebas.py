import os

def comparar(palabra, letra, cadena):
    for indice, valor in enumerate (palabra):
        if valor == letra:
            cadena[indice] = letra
            cadena_t= " ".join(cadena)
            return(cadena_t)
            
def run():
    palabra_random= list("LIBROO")
    print('!Bienvenido al juego del ahorcado!')
    print('Adivina la palabra de '+ str(len(palabra_random)) + ' letras.')
    lineas = list(len(palabra_random)*"_")
    letra= (input('Introduce una letra: ')).upper()

    # print(palabra_random)
    print (comparar(palabra_random, letra,lineas))



if __name__ == '__main__':
    run()