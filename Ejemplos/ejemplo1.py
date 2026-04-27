# ============================================================
# ejemplo1.py  -  Ciclos FOR anidados
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: Tabla de multiplicar ---
print("=" * 40)
print("  TABLA DE MULTIPLICAR (1 al 5)")
print("=" * 40)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j:<4}", end="  ")
    print()   # salto de línea al terminar cada fila

# --- Parte 2: Patrón de asteriscos ---
print("\n" + "=" * 40)
print("  TRIÁNGULO DE ASTERISCOS")
print("=" * 40)

filas = 6
for fila in range(1, filas + 1):
    for col in range(fila):
        print("*", end=" ")
    print()

# --- Parte 3: Suma de elementos de una matriz 3x3 ---
print("\n" + "=" * 40)
print("  SUMA DE FILAS EN UNA MATRIZ 3x3")
print("=" * 40)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    suma_fila = 0
    for j in range(len(matriz[i])):
        suma_fila += matriz[i][j]
        print(f"{matriz[i][j]:3}", end=" ")
    print(f"  -> suma = {suma_fila}")
