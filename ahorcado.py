import random
      
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
   
def comparar(palabra_random, letra_usr):
    palabra_guess= []
    letra= letra_usr.upper
    while palabra_random != palabra_guess:
        for i in palabra_random:
            if letra == i:
                print ("verdadero")
                break
            else:
                print ("no")
                break

        




            
# def preguntar():
#     pass

# def comparar():
#     pass

def run():
    palabra= palabra_aleatoria()
    print('!Bienvenido al juego del ahorcado!')
    print('Adivina la palabra de '+ str(len(palabra)) + ' letras.')
    print(len(palabra)*' _')
    print(palabra)
    letra=input('Introduce una letra: ')
    comparar(palabra, letra)



if __name__ == '__main__':
    run()