# ============================================================
# ejemplo3.py  -  Ordenamiento de listas y matrices
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

import random

# Generamos una lista aleatoria para ordenar
random.seed(42)
numeros = [random.randint(1, 99) for _ in range(10)]

# --- Parte 1: Ordenamiento burbuja (Bubble Sort) ---
print("=" * 45)
print("  ORDENAMIENTO BURBUJA (BUBBLE SORT)")
print("=" * 45)

burbuja = numeros[:]   # copia de la lista original
print(f"Original:   {burbuja}")

n = len(burbuja)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if burbuja[j] > burbuja[j + 1]:
            burbuja[j], burbuja[j + 1] = burbuja[j + 1], burbuja[j]

print(f"Ordenada:   {burbuja}")

# --- Parte 2: Ordenamiento por selección (Selection Sort) ---
print("\n" + "=" * 45)
print("  ORDENAMIENTO POR SELECCIÓN")
print("=" * 45)

seleccion = numeros[:]
print(f"Original:   {seleccion}")

n = len(seleccion)
for i in range(n):
    idx_min = i
    for j in range(i + 1, n):
        if seleccion[j] < seleccion[idx_min]:
            idx_min = j
    seleccion[i], seleccion[idx_min] = seleccion[idx_min], seleccion[i]

print(f"Ordenada:   {seleccion}")

# --- Parte 3: Ordenar una matriz de calificaciones por promedio ---
print("\n" + "=" * 45)
print("  ORDENAR ALUMNOS POR PROMEDIO")
print("=" * 45)

alumnos = [
    {"nombre": "Ana",    "notas": [85, 90, 78]},
    {"nombre": "Luis",   "notas": [70, 65, 80]},
    {"nombre": "Sofía",  "notas": [95, 92, 98]},
    {"nombre": "Carlos", "notas": [60, 75, 70]},
    {"nombre": "Elena",  "notas": [88, 84, 91]},
]

for alumno in alumnos:
    alumno["promedio"] = sum(alumno["notas"]) / len(alumno["notas"])

alumnos_ordenados = sorted(alumnos, key=lambda a: a["promedio"], reverse=True)

print(f"{'Nombre':<10}  {'Notas':<20}  {'Promedio':>8}")
print("-" * 45)
for a in alumnos_ordenados:
    print(f"{a['nombre']:<10}  {str(a['notas']):<20}  {a['promedio']:>8.2f}")
