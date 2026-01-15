# Variables "sueltas" (Globales, Desorganizadas)
nombre_robot = "R2D2"
bateria_robot = 95

# Función "suelta" (Opera sobre las variables sueltas)
def saludar_robot():
    global bateria_robot
    if bateria_robot > 10:
        print(f"Hola, soy {nombre_robot}. Batería: {bateria_robot}%")
        bateria_robot -= 5 # Modifica el dato global
    else:
        print(f"{nombre_robot}: ¡Batería baja! No puedo saludar.")

saludar_robot()
saludar_robot()
# ... Si tengo 20 robots, necesito 20 variables y 20 funciones... ¡un caos!