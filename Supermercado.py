


import tkinter as tk
from tkinter import messagebox
from tkinter import *
from turtle import bgcolor

def mensaje():
    variable = texto1.get()
    messagebox.showinfo(message=variable)
    variable2 = texto2.get()
    messagebox.showinfo(message=variable2)
    efectivo = radio.get()
    messagebox.showinfo(message=pagoefect)
    tarjeta = radio.get()
    messagebox.showinfo(message=pagotarj)

def pagoefect():
   precio1 = int(texto1.get())
   cantidad1 = int(texto2.get())
   total = precio1 * cantidad1
   return total

def pagotarj():
    precio2 = int(texto1.get())
    cantidad2 = int(texto2.get())
    total2 = (precio2 * cantidad2)-0.20
    return total2

ventana = tk.Tk()
ventana.geometry("300x300")
ventana.title("Supermercado")
ventana.configure(bg='purple')

radio = tk.IntVar()
texto1 = tk.Entry(ventana)
letras1 = tk.Label(ventana, text = "Precio del Producto")
texto2 = tk.Entry(ventana)
letras2 = tk.Label(ventana, text = "Cantidad del Producto")
radiobtn1 = tk.Radiobutton(ventana, text="PAGO EN EFECTIVO", value=1, variable=radio)
radiobtn2 = tk.Radiobutton(ventana, text="PAGO CON TARJETA", value=2, variable=radio)
boton1 = tk.Button(ventana, text = "PAGAR", command=mensaje, bg='blue')



texto1.grid(row=1, column=1, columnspan=2)
letras1.grid(row=1, column=3)
texto2.grid(row=4, column=1, columnspan=2)
letras2.grid(row=4, column=3)
radiobtn1.grid(row=7, column=1)
radiobtn2.grid(row=7, column=3)
boton1.grid(row=9, column=3)
ventana.mainloop()