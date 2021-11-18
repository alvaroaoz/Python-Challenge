pesos = input("¿Cuántos pesos COP tienes?: ") #se le pregunta a el usuario con input cuantos pesos tiene
pesos = float(pesos) #hacer la transformacion del valor a decimal
valor_dolar = 3875 #se asigna un valor a la variable dolar
dolares = pesos / valor_dolar #se hace la operación de la converción
dolares = round(dolares, 2) #redondea el resultado a 2 decimales
dolares = str(dolares) #se hace la convercion de numero a texto para que nos lo imprima en texto
print("Tienes $" + dolares + " dolares") #finalmente se usa la funcion de print para que nos imprima el resultado
