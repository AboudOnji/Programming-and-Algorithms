# ============================================================
# ejemploD.py  -  Ciclos WHILE y WHILE TRUE (nivel básico)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: while con contador simple ---
print("=" * 35)
print("  WHILE: CONTAR DEL 1 AL 5")
print("=" * 35)

contador = 1
while contador <= 5:
    print(f"  Contador: {contador}")
    contador += 1   # incrementar para evitar ciclo infinito

print("  Ciclo terminado.")

# --- Parte 2: while como acumulador ---
print("\n" + "=" * 35)
print("  WHILE: SUMA DEL 1 AL 10")
print("=" * 35)

numero = 1
suma   = 0

while numero <= 10:
    suma   += numero
    numero += 1

print(f"  Suma de 1 a 10 = {suma}")

# --- Parte 3: while True con break ---
print("\n" + "=" * 35)
print("  WHILE TRUE + BREAK")
print("  (máximo 4 intentos)")
print("=" * 35)

intentos = 0

while True:
    intentos += 1
    print(f"  Intento numero {intentos}")

    if intentos >= 4:
        print("  Se alcanzo el limite. Saliendo...")
        break
