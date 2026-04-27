# ============================================================
# ejemploA.py  -  Ciclos FOR anidados (nivel básico)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: Rectángulo de asteriscos ---
print("=" * 35)
print("  RECTÁNGULO DE ASTERISCOS (4 x 5)")
print("=" * 35)

for fila in range(4):          # 4 filas
    for columna in range(5):   # 5 columnas por fila
        print("*", end=" ")
    print()   # salto de línea al terminar cada fila

# --- Parte 2: Tabla de multiplicar del 1 al 3 ---
print("\n" + "=" * 35)
print("  TABLAS DEL 1, 2 Y 3  (del 1 al 5)")
print("=" * 35)

for tabla in range(1, 4):          # tablas: 1, 2, 3
    for mult in range(1, 6):       # multiplicadores: 1 al 5
        print(f"  {tabla} x {mult} = {tabla * mult}")
    print()   # línea en blanco entre tablas

# --- Parte 3: Combinaciones de frutas y colores ---
print("=" * 35)
print("  COMBINACIONES: FRUTA + COLOR")
print("=" * 35)

frutas  = ["manzana", "pera", "uva"]
colores = ["rojo", "verde"]

for fruta in frutas:
    for color in colores:
        print(f"  {fruta} - {color}")
