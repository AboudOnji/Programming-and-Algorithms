import random
lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L"]
j = 0
while True:
    name = input("Ingrese su nombre: ")
    if name == "salir":
        break
    juego = random.choice(lista)
    print("Hola", name, "tu juego es:", juego)
    j+=1
    if j ==14:
        print("Has alcanzado el límite de juegos. ¡Gracias por jugar!")
        breakd