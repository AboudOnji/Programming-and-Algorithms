# calculadora simple (sumar y multiplicar)
import tkinter as tk


def Sumar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    etiqueta_resultado.config(text=f"Resultado: {resultado}")


def Multiplicar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado2 = num1 * num2
    etiqueta_resultado.config(text=f"Resultado: {resultado2}")

# Crear la ventana principal


ventana = tk.Tk()
ventana.title("Mi primera calculadora")
ventana.geometry("800x300")
# Crear label
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_general = tk.Label(ventana, text="Calculadora para sumar dos numeros")
# crear los dos espacios para ingresar los numeros
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Crear los botones
boton_sumar = tk.Button(ventana, text="Sumar", command=Sumar)
boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=Multiplicar)
area = tk.Text(ventana, height=10, width=50)

etiqueta_general.grid(row=0, column=1, columnspan=2)
entrada1.grid(row=1, column=0)
entrada2.grid(row=2, column=0)
boton_sumar.grid(row=1, column=1)
boton_multiplicar.grid(row=2, column=1)
etiqueta_resultado.grid(row=1, column=3, columnspan=2)
area.grid(row=3, column=0, columnspan=4)

ventana.mainloop()
