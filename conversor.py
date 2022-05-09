
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    pesos = pesos / valor_dolar
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " dólares")

menu = """"
Bienvenido al conversor de monedas 🤑

1 - pesos colombianos
2 - pesos mexicanos
3 - pesos argentinos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("mexicanos", 20)
elif opcion == 3:
    conversor("argentinos", 115)
else:
    print("Por favor elige una opcion correcta")