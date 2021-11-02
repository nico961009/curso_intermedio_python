import random
import os
import time
      
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
        print('Adivina la palabra de '+ str(len(palabra)) + ' letras.')
        letra= (input('Introduce una letra: ')).upper()
        assert len(letra) == 1, "Solo se puede ingresar una letra, ni + ni -"
        assert letra.isalpha(), "Solo se pueden ingresar letras"
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
    time.sleep(3)
    os.system("clear")
    

def run():
    palabra_random= list(palabra_aleatoria())
    os.system("clear")
    print('!Bienvenido al juego del ahorcado!')
    lineas = list(len(palabra_random)*"_")
    print(" ".join(lineas))
    print(comparar(palabra_random, lineas))
    A= """¿Otra partida?
    1.- Claro        2.- Deseo seguir mi camino 
    : """
    respuesta= int(input(A))
    assert respuesta == 1 or respuesta == 2, "Solo puedes elegir entre las dos opciones mostradas en pantalla."
    if respuesta == 1:
        run()
    else:
        print("Un placer jugar contigo, vuelve pronto !")

if __name__ == '__main__':
    run()



            

