def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ") #aquí se le quita el "int" para que el assert corra correctamente.
    assert num.isnumeric() and int(num) > 0, "Solo debes de ingresar números positivos" #se utiliza el assert, junto con el método .isnumeric, para saber si el string ingresado de alguna manera es o se parece a un número.
    print(divisors(int(num))) #Se coloca ahora en esta linea el "int" para que pase como un entero a la función.
    print("Termino mi programa")

if __name__ == '__main__':
    run()