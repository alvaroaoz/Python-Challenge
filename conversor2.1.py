def conversor(tipo_pesos, valor_dolar): #se define la funcion donde se podra modularizar el codigo.
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tenes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares.")



menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("COP", 3875)
elif opcion == 2:
    conversor("ARS", 105)
elif opcion == 3:
    conversor("MXN", 24)
else:
    print('Por favor eliga una opción valida!!!') 