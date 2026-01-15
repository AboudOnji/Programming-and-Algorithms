# Juego quien hizo click

import tkinter as tk

def quien_hizo_click(fila, columna):
    etiqueta_resultado.config(text=f"El botón en fila {fila}, columna {columna} fue presionado.")   
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("¿Quién hizo click?")
ventana.geometry("400x300")
# Crear una cuadrícula de botones
for i in range(4):  # Filas
    for j in range(4):  # Columnas
        boton = tk.Button(ventana, text=f"Botón {i},{j}", font=("Arial", 12))
        boton.grid(row=i, column=j, padx=5, pady=5)
        # Usar lambda para capturar los valores actuales de i y j
        comando_celda = lambda r=i, c=j: quien_hizo_click(r, c)
        boton.config(command=comando_celda)
# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Ningún botón presionado aún.", font=("Arial", 14))
etiqueta_resultado.grid(row=4, column=0, columnspan=4, pady=10) 

ventana.mainloop()