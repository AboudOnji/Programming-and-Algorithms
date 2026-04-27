# ============================================================
# ejemplo2.py  -  Módulo RANDOM
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

import random

# --- Parte 1: Números aleatorios básicos ---
print("=" * 45)
print("  NÚMEROS ALEATORIOS BÁSICOS")
print("=" * 45)

print(f"Entero entre 1 y 100:       {random.randint(1, 100)}")
print(f"Flotante entre 0.0 y 1.0:   {random.random():.4f}")
print(f"Flotante entre 5.0 y 10.0:  {random.uniform(5.0, 10.0):.4f}")

# --- Parte 2: Lista aleatoria y elección ---
print("\n" + "=" * 45)
print("  LISTAS Y ELECCIÓN ALEATORIA")
print("=" * 45)

colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print(f"Lista original:  {colores}")

color_elegido = random.choice(colores)
print(f"Color elegido:   {color_elegido}")

random.shuffle(colores)
print(f"Lista mezclada:  {colores}")

muestra = random.sample(colores, 3)
print(f"Muestra de 3:    {muestra}")

# --- Parte 3: Simulación de dados (10 lanzamientos) ---
print("\n" + "=" * 45)
print("  SIMULACIÓN: 10 LANZAMIENTOS DE DADO")
print("=" * 45)

conteo = {i: 0 for i in range(1, 7)}

for lanzamiento in range(1, 11):
    resultado = random.randint(1, 6)
    conteo[resultado] += 1
    print(f"  Lanzamiento {lanzamiento:2}: {resultado}")

print("\nFrecuencia de cada cara:")
for cara, veces in conteo.items():
    print(f"  Cara {cara}: {'|' * veces} ({veces})")
