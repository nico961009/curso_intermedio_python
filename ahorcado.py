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
    palabra_random= list(palabra_aleatoria())
    os.system("clear")
    print('!Bienvenido al juego del ahorcado!')
    print('Adivina la palabra de '+ str(len(palabra_random)) + ' letras.')
    lineas = list(len(palabra_random)*"_")
    print(" ".join(lineas))
    print(comparar(palabra_random, lineas))




if __name__ == '__main__':
    run()



            

