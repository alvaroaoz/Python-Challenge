# def imprimir_mensaje(): #funciones con def
#    print('Mensaje especial: ')
#   print('¡Estoy aprendiendo a usar funciones!')


#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()


def conversacion(mensaje): #parametros son variables que tendre disponibles para usarla dentro de las funciones.
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion ==3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe la opcion correcta')