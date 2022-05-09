import random

def run():
    numero_aleatorio = random.randint(1, 100)
    vida = 5
    print("Tienes " + str(vida) + " vidas")
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            vida -= 1
            print("Busca un número más grande")
        elif numero_elegido > numero_aleatorio:
            vida -= 1
            print("Busca un número más pequeño")
        else:
            print("Ganaste!")
        if vida == 0:
            print("GAME OVER")
            break
        print("Tienes " + str(vida) + " vidas")
        numero_elegido = int(input("Elige otro número: "))


if __name__ == "__main__":
    run()