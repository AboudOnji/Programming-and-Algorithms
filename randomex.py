import random
import numpy as np
import math


# crear una matriz de 3x3 con números aleatorios entre 1 y 100
matrix = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        matrix[i][j]=random.randint(1, 100)
print("Matriz original:")
print(matrix)

# ---- Ejemplos de ordenamiento de la matriz ----

# 1. Ordenar todos los elementos (aplanar, ordenar y reconstruir)
flat_sorted = np.sort(matrix, axis=None)  # ordena todos los elementos
print("\n1. Todos los elementos ordenados (aplanado):")
print(flat_sorted)


# 2. Ordenar cada fila de menor a mayor
sorted_rows = np.sort(matrix, axis=1)
print("\n2. Cada fila ordenada de menor a mayor:")
print(sorted_rows)

# 3. Ordenar cada columna de menor a mayor
sorted_cols = np.sort(matrix, axis=0)
print("\n3. Cada columna ordenada de menor a mayor:")
print(sorted_cols)

# 4. Ordenar en orden descendente (cada fila)
sorted_desc = np.sort(matrix, axis=1)[:, ::-1]
print("\n4. Cada fila ordenada de mayor a menor:")
print(sorted_desc)

# 5. Ordenar en orden descendente (cada columna)
sorted_cols_desc = np.sort(matrix, axis=0)[::-1, :]
print("\n5. Cada columna ordenada de mayor a menor:")
print(sorted_cols_desc)

# 6. Obtener los índices que ordenarían cada fila
argsort_rows = np.argsort(matrix, axis=1)
print("\n6. Índices que ordenan cada fila (argsort):")
print(argsort_rows)

# 7. Valor mínimo y máximo de la matriz
print(f"\n7. Valor mínimo: {matrix.min()}, posición: {np.unravel_index(matrix.argmin(), matrix.shape)}")
print(f"   Valor máximo: {matrix.max()}, posición: {np.unravel_index(matrix.argmax(), matrix.shape)}")
