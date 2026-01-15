import tkinter as tk


def ventana_uno():
    nueva = tk.Toplevel()
    nueva.title("Ventana Uno")
    nueva.geometry("300x200")
    tk.Label(nueva, text="Esta es la primera ventana").pack(pady=20)
    tk.Button(nueva, text="Cerrar", command=nueva.destroy).pack()


def ventana_dos():
    nueva = tk.Toplevel()
    nueva.title("Ventana Dos")
    nueva.geometry("300x200")
    tk.Label(nueva, text="Esta es la segunda ventana").pack(pady=20)
    tk.Button(nueva, text="Cerrar", command=nueva.destroy).pack()


def ventana_tres():
    nueva = tk.Toplevel()
    nueva.title("Ventana Tres")
    nueva.geometry("300x200")
    tk.Label(nueva, text="Esta es la tercera ventana").pack(pady=20)
    tk.Button(nueva, text="Cerrar", command=nueva.destroy).pack()


ventana = tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("400x300")

tk.Label(ventana, text="Selecciona una opcion:").pack(pady=10)

boton1 = tk.Button(ventana, text="Abrir Ventana 1", command=ventana_uno)
boton1.pack(pady=5)

boton2 = tk.Button(ventana, text="Abrir Ventana 2", command=ventana_dos)
boton2.pack(pady=5)

boton3 = tk.Button(ventana, text="Abrir Ventana 3", command=ventana_tres)
boton3.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack(pady=20)

ventana.mainloop()
