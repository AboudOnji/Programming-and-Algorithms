import tkinter as tk
def saludar():
    nombre_usuario = nombre.get()
    muestra.config(text=f"¡Hola, {nombre_usuario}! Bienvenido/a a la app.")
    ventana_nueva = tk.Toplevel()
    ventana_nueva.title("Ventana de Saludo")
    ventana_nueva.geometry("400x200")
    mensaje = tk.Label(ventana_nueva, text=f"¡Hola, {nombre_usuario}! Esta es una ventana nueva.", font=("Arial", 16))
    mensaje.pack()
def cerrar_ventana(event):
    print(f'Clic en la posicion: {event.x}, {event.y}')
    ventana.destroy()
   
    
ventana = tk.Tk()
ventana.title("Saludador con Clases")
ventana.geometry("800x1200")

texto = tk.Label(ventana, text="Ingrese su nombre:", font=("Arial", 24))
nombre = tk.Entry(ventana)
accion = tk.Button(ventana, text="Saludar", command = saludar, bg="red", fg="white", font=("Arial", 18))
muestra = tk.Label(ventana, text="", font=("Arial", 18))
imagen = tk.PhotoImage(file="imagen.png")
etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.bind("<Button-1>", cerrar_ventana)
texto.grid(row=0, column=0)
nombre.grid(row=0, column=1)
accion.grid(row=1, column=0)
muestra.grid(row=2, column=0)
etiqueta_imagen.grid(row=3, column=0)

#etiqueta_imagen.pack()
#texto.pack()
#nombre.pack()
#accion.pack()
#muestra.pack()
ventana.mainloop()
