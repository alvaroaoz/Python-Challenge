menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos COP tenes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares.")
elif opcion == 2:
    pesos = input("¿Cuántos pesos ARS tenes?: ")
    pesos = float(pesos)
    valor_dolar = 105
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " Dolares.")
elif opcion == 3:
    pesos = input("¿Cuántos pesos MXN tenes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " Dolares.")
else:
    print('Por favor eliga una opción valida!!!') # Está mal esto ya que se repite mucho una misma logica lo que hace que sea menos elegante el codigo.