import tkinter as tk

class AplicacionSaludador(tk.Frame):
    
    # El constructor. Se ejecuta al crear la instancia de la clase.
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Saludador CON Clases")
        self.pack()
        self.crear_widgets()
    
    def crear_widgets(self):

        self.entrada_nombre = tk.Entry(self, width=30)
        self.entrada_nombre.pack()

        self.boton_saludar = tk.Button(self, 
                                       text="Saludar", 
                                       command=self.saludar) 
        self.boton_saludar.pack()

        self.etiqueta_resultado = tk.Label(self, text="Esperando nombre...")
        self.etiqueta_resultado.pack()

    def saludar(self):
        nombre = self.entrada_nombre.get()
        self.etiqueta_resultado.config(text=f"¡Hola, {nombre}! Bienvenido/a a la app.")

# --- Código Principal (Mínimo y Limpio) ---
if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    # 4. Crea una instancia de la aplicación
    app = AplicacionSaludador(master=ventana_raiz)
    app.mainloop()