pesos = input("¿Cuántos pesos ARS tenes?: ")
pesos = float(pesos)
valor_dolar = 105
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " Dolares.")

dolares = input("¿Cuántos dolares U$D tenes?: ")
dolares = float(dolares)
valor_pesos = 105
pesos = dolares * valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print ("Tienes $" + pesos + " pesos ARS.")