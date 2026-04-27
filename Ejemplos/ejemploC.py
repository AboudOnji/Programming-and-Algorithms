# ============================================================
# ejemploC.py  -  Ordenamiento de listas (nivel básico)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: .sort() — ordenar una lista de números ---
print("=" * 40)
print("  .sort() — NÚMEROS ASCENDENTE")
print("=" * 40)

calificaciones = [75, 90, 60, 85, 70, 95, 65]
print(f"  Original:    {calificaciones}")

calificaciones.sort()            # modifica la lista en su lugar
print(f"  Ascendente:  {calificaciones}")

# --- Parte 2: .sort(reverse=True) — ordenar descendente ---
print("\n" + "=" * 40)
print("  .sort(reverse=True) — DESCENDENTE")
print("=" * 40)

puntajes = [55, 88, 72, 99, 61, 80]
print(f"  Original:    {puntajes}")

puntajes.sort(reverse=True)
print(f"  Descendente: {puntajes}")

# --- Parte 3: sorted() — ordenar sin modificar el original ---
print("\n" + "=" * 40)
print("  sorted() — NOMBRES ALFABÉTICO")
print("=" * 40)

nombres = ["Carlos", "Ana", "Sofia", "Luis", "Maria", "Beto"]
print(f"  Original:    {nombres}")

nombres_ordenados = sorted(nombres)         # NO modifica nombres
print(f"  Ordenados:   {nombres_ordenados}")
print(f"  Original ok: {nombres}")          # sigue igual
