# ============================================================
# ejemploE.py  -  MATCH / CASE — switch-case (nivel básico)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: Día de la semana ---
print("=" * 40)
print("  DÍA DE LA SEMANA")
print("=" * 40)

for numero in range(1, 9):       # del 1 al 8 (8 es inválido)
    match numero:
        case 1:
            dia = "Lunes"
        case 2:
            dia = "Martes"
        case 3:
            dia = "Miercoles"
        case 4:
            dia = "Jueves"
        case 5:
            dia = "Viernes"
        case 6:
            dia = "Sabado"
        case 7:
            dia = "Domingo"
        case _:
            dia = "Numero invalido"
    print(f"  Dia {numero}: {dia}")

# --- Parte 2: Semáforo ---
print("\n" + "=" * 40)
print("  SEMAFORO")
print("=" * 40)

colores = ["rojo", "amarillo", "verde", "azul"]

for color in colores:
    match color:
        case "rojo":
            accion = "Detente"
        case "amarillo":
            accion = "Precaucion"
        case "verde":
            accion = "Avanza"
        case _:
            accion = "Color no reconocido"
    print(f"  {color:<10} -> {accion}")

# --- Parte 3: Calificación en letra ---
print("\n" + "=" * 40)
print("  CALIFICACIÓN EN LETRA")
print("=" * 40)

letras = ["A", "B", "C", "D", "F", "X"]

for letra in letras:
    match letra:
        case "A":
            descripcion = "Excelente  (90 - 100)"
        case "B":
            descripcion = "Bien       (80 - 89)"
        case "C":
            descripcion = "Suficiente (70 - 79)"
        case "D":
            descripcion = "Minimo     (60 - 69)"
        case "F":
            descripcion = "Reprobado  (< 60)"
        case _:
            descripcion = "Letra no reconocida"
    print(f"  {letra}: {descripcion}")
