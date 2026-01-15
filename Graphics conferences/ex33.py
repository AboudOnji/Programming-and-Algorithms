import tkinter as tk


def dona():
    ventana_nueva = tk.Toplevel()
    ventana_nueva.title("Ventana nueva")
    ventana_nueva.geometry("400x300")
    boton3 = tk.Button(ventana_nueva, text="Cerrar",
                       command=ventana_nueva.destroy)
    boton3.grid(row=0, column=0)
    a = int(jugador.get())
    for i in range(a):
        boton4 = tk.Button(ventana_nueva, text=f"Jugador {i+1}")
        boton4.grid()


ventana = tk.Tk()
ventana.title("Juego sin chiste")
ventana.geometry("400x300")
jugador = tk.Entry()
jugador.grid(row=2, column=0)

etiqueta = tk.Label(text="Pica el boton")
boton1 = tk.Button(text="venta nueva", command=dona)
boton2 = tk.Button(text="cerrar", command=ventana.destroy)
etiqueta.grid(row=0, column=0)
boton1.grid(row=0, column=1, padx=10, pady=10)
boton2.grid(row=1, column=10)

ventana.mainloop()
