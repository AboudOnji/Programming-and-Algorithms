# ============================================================
# ejemplo4.py  -  Ciclos WHILE y WHILE TRUE
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

import random

# --- Parte 1: While con contador ---
print("=" * 45)
print("  WHILE: POTENCIAS DE 2")
print("=" * 45)

potencia = 1
n = 0
while potencia <= 512:
    print(f"  2^{n:2} = {potencia}")
    n += 1
    potencia *= 2

# --- Parte 2: While con condición de convergencia ---
print("\n" + "=" * 45)
print("  WHILE: ALGORITMO DE LA RAÍZ CUADRADA")
print("  (Método de Newton-Raphson)")
print("=" * 45)

objetivo = 50.0
x = objetivo / 2.0        # estimación inicial
tolerancia = 1e-6
iteracion = 0

while abs(x * x - objetivo) > tolerancia:
    x = (x + objetivo / x) / 2.0
    iteracion += 1

print(f"  sqrt({objetivo}) ≈ {x:.8f}  (en {iteracion} iteraciones)")
print(f"  Verificación: {x:.8f}² = {x*x:.8f}")

# --- Parte 3: While True con break y continue ---
print("\n" + "=" * 45)
print("  WHILE TRUE: JUEGO DE ADIVINAR EL NÚMERO")
print("  (modo demo: el programa 'adivina' solo)")
print("=" * 45)

secreto = random.randint(1, 20)
intentos = 0
limite = 10
bajo, alto = 1, 20

print(f"  Número secreto oculto entre 1 y 20")

while True:
    if intentos >= limite:
        print(f"  Se agotaron los {limite} intentos. El número era {secreto}.")
        break

    intento = (bajo + alto) // 2   # búsqueda binaria automática
    intentos += 1

    if intento == secreto:
        print(f"  Intento {intentos}: {intento} -> ¡CORRECTO! Encontrado en {intentos} intentos.")
        break
    elif intento < secreto:
        print(f"  Intento {intentos}: {intento} -> muy bajo")
        bajo = intento + 1
        continue
    else:
        print(f"  Intento {intentos}: {intento} -> muy alto")
        alto = intento - 1
        continue
