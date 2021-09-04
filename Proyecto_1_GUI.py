import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("Proyecto 1 de Diseño Lógico")

#Base
#canvas = tk.Canvas(root, width =  700, height = 600)
#canvas.grid(columnspan = 3,rowspan = 2)

#Ingresar texto y calcular
tit = Label(root, text= "Favor ingresar un numero octal de 4 digitos unicamente")
tit.grid(row=0, column=0, columnspan = 2)

n = Entry(root, width=45, borderwidth=5)
n.grid(row = 1, column = 0 , columnspan = 1, padx = 10, pady = 10)

cal = Button(root, text="Calcular",command = lambda:ingDato(n.get()))
cal.grid(row = 1, column = 2)

#Crea la tabla de conversiones
def genTabla(hex,bin,dec):
    conver = [("Hexadecimal", hex), ("Binario",bin),("Decimal",dec)]
    rows = len(conver)
    colum = len(conver[0])

    for i in range(rows):
        for j in range(colum):
            e = Label(root, width = 20, text= conver[i][j] )
            e.grid(row = i+2,column = j)

#Ingresa los Datos y los valida
def ingDato(dato):  
    dato = int(dato) 
    cuatro = False
    num = False
    if dato == 0:
        messagebox.showerror("ERROR","Favor ingresar numero")
    else: 
        num = True

    oct = 0

    #Determinar si es de 4 digitos
    if num == True:
        dato = str(dato)
        if len(dato) > 4 or num == False:

            messagebox.showerror("ERROR","El número ingresado tiene mas de 4 digitos, favor ingresar otro numero")
        else:
            cuatro = True
        
    if cuatro == True:
    #Determinar si es numero Octal    
        for i in dato:
            if i >= "8":
                oct =+ 1
        if oct != 0:
            messagebox.showerror("ERROR","Numero NO es Octal, favor ingrese otro numero")
            dato = ""
        else:
            dato = int(dato)
            ndeci = octToDec(dato)
            genTabla(octToHex(ndeci),octToBin(ndeci),ndeci)

#Convierte el numero en Decimal
def octToDec(dato):
    dato = str(dato)
    n10 = 0 #Variable donde se va a almacenar el dato convertido a decimal

    for i in range(0,len(dato)):
        n10 += int(dato[len(dato)-1-i])*pow(8,i) #recorre el dato y hace lo necesario para convertirlo a decimal

    return n10 #:devuelve el dato convertido para que pueda ser usado para las otras conversiones (hex y bin)

#Convierte el numero a Binario
def octToBin(n10):
    d = n10 
    abin = []

    while d != 0:
        div = d // 2
        r = d % 2
        abin.append(r)
        d = div

    sum = 0
    n2 = 0

    for i in range(0,len(abin)):
        n2 += abin[i]*(pow(10,i))

    return n2

#Convertir numero a Hexadecimal
def octToHex(n10):
    h = n10
    shex = ""
    hexa = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    while h != 0:
        div = h // 16
        r = h % 16
        shex += hexa[r]
        h = div

    nhex = ""

    for i in range(0,len(shex)):
        nhex += shex[len(shex) - 1 -i]

    return nhex


root.mainloop()
