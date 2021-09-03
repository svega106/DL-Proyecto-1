import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from tkinter import ttk

root = Tk()

texto = Label(root, text = "Digite un numero octal de 4 digitos")
boton = Button(root, text = "Calcular")

canvas = tk.Canvas(root, height= 450, width= 900, bg= "#263d42")
lb = Label(root, text = "Hola")
lb.grid(row=0,column=0)

canvas.grid(row=0,column=1)

frame = tk.Frame(root,background= "#3e646c")
frame.place(relwidth = 0.8, relheight = 0.8, relx= 0.1, rely= 0.1)

#Crear la tabla

  
root.mainloop()
  

