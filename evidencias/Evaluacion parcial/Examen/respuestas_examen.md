## Respuestas de examen parcial 2

## Materia: Algoritmos y Programación

## Prof. Dr. Aboud Barsekh Onji

---

## Sección A — Opción Múltiple

**P1 — a) y c)**

- `range(1, 10, 2)` → 1,3,5,7,9 **(correcto)**

- `range(1, 11, 2)` → 1,3,5,7,9 **(correcto)** (se detiene antes de llegar a 11)

- `range(0,10,2)` da pares; `range(9,0,-2)` da orden inverso

**P2 — b) 4**

Positivos en la lista: 3, 7, 5, 8 → `contador = 4`

**P3 — a), b) y c)**

- `len` = 5 **(correcto)**, `sum` = 34 **(correcto)**, `max` = 10 **(correcto)**

- `datos[4]` = 10 (no 3) **(incorrecto)**

**P4 — b) `[5, 15, 20, 20]`**

`pop(1)` quita el 10 → lista queda `[5,15,20]`; se agrega `10*2=20`

**P5 — a), b) y d)**

- Imprime `B` **(correcto)**; el `elif >= 70` nunca se evalúa **(correcto)**; con 65 imprimiría `F` **(correcto)**

- Con 90 solo imprimiría `A` (no ambas) **(incorrecto)**

**P6 — a), b) y c)**

`random.choice([])` lanza `IndexError`, no devuelve `None` **(incorrecto)**

**P7 — a), b) y d)**

Suma 1+2+3+4+5 = 15; ciclo corre 5 veces; al salir `n = 6`

**P8 — a), b) y d)**

`range(6)` incluye el 0 por lo que genera `[0,1,4,9,16,25]` **(incorrecto)**

---

## Sección B

### Problema 1

```python
calificaciones = [78, 92, 55, 63, 88, 45, 71, 96, 60, 83]

i = 0
while i < len(calificaciones):
    if calificaciones[i] >= 70:
        print(calificaciones[i], "Aprobado")
    else:
        print(calificaciones[i], "Reprobado")
    i += 1

promedio = sum(calificaciones) / len(calificaciones)
print("Promedio:", promedio)

print("Calificacion mas alta:", max(calificaciones))

eliminada = calificaciones.pop()
print("Calificacion eliminada:", eliminada)

calificaciones.append(74)
print("Lista final:", calificaciones)
```

### Problema 2

```python
import random

resultados = []

for i in range(10):
    lanzamiento = random.randint(1, 6)
    resultados.append(lanzamiento)

print("Resultados:", resultados)

conteo_seises = 0
for r in resultados:
    if r == 6:
        conteo_seises += 1
print("Numero de seises:", conteo_seises)

total = sum(resultados)
if total >= 40:
    print("Puntuacion alta")
elif total >= 25:
    print("Puntuacion media")
else:
    print("Puntuacion baja")
```

---


