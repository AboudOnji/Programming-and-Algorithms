import tkinter as tk


class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi primera calculadora (Clases)")
        self.root.geometry("800x300")

        self.crear_interfaz()

    def crear_interfaz(self):
        # Etiqueta general
        self.etiqueta_general = tk.Label(
            self.root, text="Calculadora para sumar dos numeros (POO)")
        self.etiqueta_general.grid(row=0, column=1, columnspan=2)

        # Entradas
        self.entrada1 = tk.Entry(self.root)
        self.entrada1.grid(row=1, column=0)

        self.entrada2 = tk.Entry(self.root)
        self.entrada2.grid(row=2, column=0)

        # Botones
        self.boton_sumar = tk.Button(
            self.root, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(row=1, column=1)

        self.boton_multiplicar = tk.Button(
            self.root, text="Multiplicar", command=self.multiplicar)
        self.boton_multiplicar.grid(row=2, column=1)

        # Etiqueta de resultado
        self.etiqueta_resultado = tk.Label(self.root, text="Resultado: ")
        self.etiqueta_resultado.grid(row=1, column=3, columnspan=2)

        # Area de texto
        self.area = tk.Text(self.root, height=10, width=50)
        self.area.grid(row=3, column=0, columnspan=4)

    def sumar(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            resultado = num1 + num2
            self.etiqueta_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.etiqueta_resultado.config(
                text="Error: Ingrese números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            resultado = num1 * num2
            self.etiqueta_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.etiqueta_resultado.config(
                text="Error: Ingrese números válidos")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraApp(ventana)
    ventana.mainloop()
