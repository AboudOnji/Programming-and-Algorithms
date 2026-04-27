# ============================================================
# ejemploB.py  -  Módulo RANDOM (nivel básico)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

import random

# --- Parte 1: Lanzar un dado 5 veces ---
print("=" * 35)
print("  DADO DE 6 CARAS — 5 LANZAMIENTOS")
print("=" * 35)

for lanzamiento in range(1, 6):
    resultado = random.randint(1, 6)
    print(f"  Lanzamiento {lanzamiento}: {resultado}")

# --- Parte 2: Elegir un ganador al azar ---
print("\n" + "=" * 35)
print("  SORTEO DE GANADOR")
print("=" * 35)

participantes = ["Ana", "Luis", "Sofia", "Carlos", "Maria"]
print(f"  Participantes: {participantes}")

ganador = random.choice(participantes)
print(f"  El ganador es: {ganador}")

# --- Parte 3: Lanzar una moneda 6 veces y contar ---
print("\n" + "=" * 35)
print("  MONEDA — 6 LANZAMIENTOS")
print("=" * 35)

caras  = 0
sellos = 0

for i in range(1, 7):
    resultado = random.choice(["Cara", "Sello"])
    print(f"  Lanzamiento {i}: {resultado}")
    if resultado == "Cara":
        caras += 1
    else:
        sellos += 1

print(f"\n  Total caras:  {caras}")
print(f"  Total sellos: {sellos}")
