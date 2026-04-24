#código para diseño gráfico

import tkinter as tk

def sumar():
    n = entrada_nombre.get()


def saludar():
    nombre = entrada_nombre.get()
    etiqueta_resultados.config(text="Hola " + nombre)

# Función para crear una ventana
def crear_ventana():
    def dividir_ventana():
        
        

    ventana = tk.Tk()
    ventana.title("Mi aplicación")
    ventana.geometry("400x300")
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)
    return ventana

ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("400x300")
ventana.config(bg="blue")
etiquetainst=tk.Label(ventana, text="Escribe tu nombre")
entrada_nombre = tk.Entry(ventana)
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_crear = tk.Button(ventana, text="Crear ventana", command=crear_ventana)
etiqueta_resultados=tk.Label(ventana, text="")

etiquetainst.pack(pady=10)
entrada_nombre.pack(pady=10)
boton_saludar.pack(pady=10)
boton_crear.pack(pady=10)
etiqueta_resultados.pack(pady=10)

ventana.mainloop()

