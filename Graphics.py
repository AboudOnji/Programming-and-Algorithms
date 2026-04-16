#código para diseño gráfico

import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    etiqueta_resultados.config(text="Hola " + nombre)


ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("400x300")
ventana.config(bg="blue")
etiquetainst=tk.Label(ventana, text="Escribe tu nombre")
entrada_nombre = tk.Entry(ventana)
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
etiqueta_resultados=tk.Label(ventana, text="")

etiquetainst.pack(pady=10)
entrada_nombre.pack(pady=10)
boton_saludar.pack(pady=10)
etiqueta_resultados.pack(pady=10)

ventana.mainloop()

