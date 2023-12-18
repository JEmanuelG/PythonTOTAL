import random


intentos = 0
jugador = str()
opcion = int()
numero = random.randint(1, 101)

print("Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
#print(f"random: {numero}")

while intentos < 8:
    opcion = int(input("Que número he pensado?\nResponde:"))
    intentos += 1
    
    if opcion < 1 or opcion > 100:
        print("Ha elegido un número que no está permitido")
    
    elif opcion < numero:
        print("Su respuesta es incorrecta, ha elegido un número MENOR al número secreto.")

    elif opcion > numero:
        print("Su respuesta es incorrecta, ha elegido un número MAYOR al número secreto.")

    elif opcion == numero:
        print("Felicitaciones!! Ha ganado.")
        print(f"Te tomó {intentos} intentos.")
        break
    
    if intentos == 8:
        print("Los siento, no adivinaste el número.")