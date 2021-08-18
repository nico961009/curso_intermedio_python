import random
import os
      
def palabra_aleatoria():
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        my_list= []
        for i in (f):
            my_list.append(i)
        palabra_aleatoria = str(random.choice (list(my_list)))
        palabra_aleatoria= palabra_aleatoria.strip()
        palabra_aleatoria= palabra_aleatoria.upper()
    cadena= str(palabra_aleatoria)
    mapeo= {
        ord('Á'): 'A',
        ord('É'): 'E',
        ord('Í'): 'I',
        ord('Ó'): 'O',
        ord('Ú'): 'U',        
    }
    cadena= cadena.translate(mapeo)
    return cadena

def comparar(palabra_random, letra, lineas):
    show =[lineas]
    while palabra_random != show:
        for i in palabra_random():
            if letra == palabra_random[i]:
                show.replace(show[i], letra)
                return show
            else:
                return "horrible"




def run():
    palabra_random= palabra_aleatoria()
    print('!Bienvenido al juego del ahorcado!')
    print('Adivina la palabra de '+ str(len(palabra_random)) + ' letras.')
    lineas = print(len(palabra_random)*' _')
    print(palabra_random)
    letra= input('Introduce una letra: ').upper
    print (comparar(palabra_random, letra, lineas))



if __name__ == '__main__':
    run()


vreijbntrjnevwrjekmcrokemrijvmtrijvrij