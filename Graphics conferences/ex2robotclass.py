

class Robot:
    def __init__(self, nombre_inicial, bateria_inicial):
        # 1. Los datos ahora se guardan DENTRO del robot usando 'self.'
        self.nombre = nombre_inicial
        self.bateria = bateria_inicial

    def saludar(self):
        if self.bateria > 10:
            # 2. Accede a sus propios datos con 'self.'
            print(f"Hola, soy {self.nombre}. Batería: {self.bateria}%")
            self.bateria -= 5
        else:
            print(f"{self.nombre}: ¡Batería baja! No puedo saludar.")


# Creamos DOS robots a partir del mismo molde
robot_a = Robot("Wall-E", 100)  # Este es un objeto 'Robot'
robot_b = Robot("Eve", 50)    # Este es OTRO objeto 'Robot'

print("--- Turno de Wall-E ---")
robot_a.saludar()  # Wall-E saluda, usa su propia batería (100 -> 95)
print(f"Batería de Wall-E: {robot_a.bateria}%")

print("\n--- Turno de Eve ---")
robot_b.saludar()  # Eve saluda, usa su propia batería (50 -> 45)
print(f"Batería de Eve: {robot_b.bateria}%")

# ¡Sus datos están separados y organizados!
# Los datos (atributos) y la acción (métodos) de 'robot_a' no afectan a 'robot_b'.
