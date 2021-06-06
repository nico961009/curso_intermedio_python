DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs= [worker["name"] for worker in DATA if worker["language"]== "python"] #al inicio worker["name"] es el valor que se retorna, en este caso el value de name o nombre.
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA)) #esto me va a regresar todos los mayores de edad, pero no regresará solo su nombre sino que regresará el diccionario completo.
    adults = list(map(lambda worker: worker["name"],adults))# con esta linea de código lo que hago es extraer el nombre de la lista adults únicamente y así evitamos mostrar todo el diccionario. Notar que se hizó doble filtro.
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) #en el primer parámetro de "map" tenemos le decimos al programa que quiero que el diccionario contenido en "worker" se una con un nuevo diccionario, esto mediante el "pipe(|)" -> Forma de sumar diccionarios. El nuevo diccionario o llave tendrá el valor false o true dependiendo del valor de age.

    for worker in old_people: #En este "for" con solo cambiar por el nombre de las listas, es suficiente para ejecutar cada una de ellas.
        print (worker)

if __name__ == '__main__':
    run()