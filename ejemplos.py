import random

alumnos = [
    "Yun", "Abraham", "Karla", "Carlos",
    "Jose Maria", "Regina", "Antonio", "Rodrigo"
]

proyectos = [
    "Proyecto 1", "Proyecto 2", "Proyecto 3", "Proyecto 4",
    "Proyecto 5", "Proyecto 6", "Proyecto 7", "Proyecto 8",
    "Proyecto 9", "Proyecto 10"
]

proyectos_disponibles = proyectos.copy()

print("=== SORTEO DE PROYECTOS ===\n")

for alumno in alumnos:
    proyecto = random.choice(proyectos_disponibles)
    proyectos_disponibles.remove(proyecto)
    print(f"{alumno}  →  {proyecto}")

print(f"\nProyectos no asignados: {proyectos_disponibles}")
