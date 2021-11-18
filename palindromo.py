def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): #buena practica crear una funcion principal que correra desde el principio puede ser run o main que se le puede colocar
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':#el entri point o punto de entrada, una vez que se encuentra py con esto ejecuta todo lo que esta debajo, se pone en todos por buena practica
    run()
# def run():
