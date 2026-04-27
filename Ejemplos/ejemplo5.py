# ============================================================
# ejemplo5.py  -  MATCH / CASE (Switch-Case en Python 3.10+)
# Materia: Algoritmos y Programación en Python
# Prof. Dr. Aboud Barsekh-Onji  |  Universidad Anáhuac México
# ============================================================

# --- Parte 1: Calculadora simple con match-case ---
print("=" * 45)
print("  CALCULADORA SIMPLE")
print("=" * 45)

def calculadora(a, operacion, b):
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: división entre cero"
            return a / b
        case "**":
            return a ** b
        case _:
            return f"Operación '{operacion}' no reconocida"

operaciones = [(10, "+", 5), (10, "-", 3), (4, "*", 7),
               (15, "/", 4), (2, "**", 8), (9, "/", 0), (3, "%", 2)]

for a, op, b in operaciones:
    resultado = calculadora(a, op, b)
    print(f"  {a:>4} {op:>2} {b:<4} = {resultado}")

# --- Parte 2: Clasificación de figuras geométricas ---
print("\n" + "=" * 45)
print("  CLASIFICACIÓN DE FIGURAS")
print("=" * 45)

def clasificar_figura(lados):
    match lados:
        case 3:
            return "Triángulo"
        case 4:
            return "Cuadrilátero (cuadrado, rectángulo...)"
        case 5:
            return "Pentágono"
        case 6:
            return "Hexágono"
        case n if n > 6:
            return f"Polígono de {n} lados"
        case _:
            return "Figura no válida"

for lados in [3, 4, 5, 6, 8, 12, 1]:
    print(f"  {lados} lados -> {clasificar_figura(lados)}")

# --- Parte 3: Sistema de menú con match-case ---
print("\n" + "=" * 45)
print("  SIMULACIÓN DE MENÚ DE SISTEMA")
print("=" * 45)

comandos = ["inicio", "ayuda", "salir", "config", "datos", "desconocido"]

def ejecutar_comando(cmd):
    match cmd:
        case "inicio":
            return "Sistema iniciado correctamente."
        case "ayuda":
            return "Comandos: inicio | ayuda | salir | config | datos"
        case "salir":
            return "Cerrando sesión..."
        case "config":
            return "Abriendo configuración del sistema."
        case "datos":
            return "Cargando módulo de datos."
        case _:
            return f"Comando '{cmd}' no reconocido. Escribe 'ayuda'."

for cmd in comandos:
    print(f"  > {cmd:<15} -> {ejecutar_comando(cmd)}")
