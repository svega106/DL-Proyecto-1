import tkinter as tk
from tkinter import *   
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog, Text
import numpy as np
import matplotlib.pyplot as plt

root = Tk()

root.title("Proyecto 1 de Diseño Lógico")

#Base
#canvas = tk.Canvas(root, width =  700, height = 600)
#canvas.grid(columnspan = 3,rowspan = 2)

#Ingresar texto y calcular
tit = Label(root, text= "Favor ingresar un numero octal de 4 digitos unicamente")
tit.grid(row=0, column=0, columnspan = 3)

n = Entry(root, width=45, borderwidth=5)
n.grid(row = 1, column = 0 , columnspan = 1, padx = 10, pady = 10)

cal = Button(root, text="Calcular",command = lambda:ingDato(n.get()))
cal.grid(row = 1, column = 2)

def segundaParte():
    tit2 = Label(root, text = "Codificacion NRZI")
    tit2.grid(row = 5, column = 0, columnspan = 3)
    nr = Label(root, text = nrzi(octToBin(octToDec(n.get()))))
    nr.grid(row = 6, column = 0, columnspan = 2)
    nrzbut = Button(root, text = "Generar grafica de NRZI", command = lambda:crearGrafico(nrzi(octToBin(octToDec(n.get())))))
    nrzbut.grid(row = 6, column = 1)

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
    cuatro = False
    num = False
    if dato == "":
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
            segundaParte()
            

#Convierte el numero en Decimal
def octToDec(dato):
    dato = str(dato)
    n10 = 0 #Variable donde se va a almacenar el dato convertido a decimal

    for i in range(0,len(dato)):
        n10 += int(dato[len(dato)-1-i])*pow(8,i) #recorre el dato y hace lo necesario para convertirlo a decimal

    return n10 #:devuelve el dato convertido para que pueda ser usado para las otras conversiones (hex y bin)

#Convierte el numero a Binario
def octToBin(n10):
    d = int(n10)
    abin = []

    while d != 0:
        div = d // 2
        r = d % 2
        abin.append(r)
        d = div

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

def nrzi(datoBin):
    valAnt = '1'  #inico de la señal en alto o bajo, alto = 1, bajo = 0
    datoBin = str(datoBin) #el dato es entero, se comvierte a texto para manerjarlo de manera mas facil
    datoTemporal = ''      
    
    nrziCode = '' # Donde se va a almacenar el codigo nrzi
    
    """El siguiente if compara si el dato entero tiene menos de 12 digitos, esto porque python no acepta ceros a la izquierda,
        este if agrega esos ceros que hacen falta, por ejemplo: 100-> 000000000100 """
    if len(datoBin) < 13:
        datoTemporal = ( ( 12-len(datoBin) )*'0' ) + datoBin
        datoBin = datoTemporal
    """ El siguiente for compara si hay un uno, si hay un uno, agrega un cambio en la señal, como se explica en el funcionamiento de codigo nrzi, usa """    
    for i in datoBin:
        if i == '1':
            nrziCode += dif(valAnt)
            valAnt = dif(valAnt)
        else:
            nrziCode += valAnt
            valAnt = valAnt
    return nrziCode

def dif(d):#funcion que devuelve el caracter contrario a otro caracter

    x = str(d)
    if x == '1':
        return str(0)
    elif x == '0':
        return str(1)

#Crea la grafica de NRZI
def crearGrafico(nrziCode):
    
    #nrziCode = "100000101001"#desactivar en cuando se haya agregado al programa principal, 
          #"010000100111"

    bipolar = -1# 0 para que la onda no sea bipolar, -1 para que sea bipolar
    x = [0,1]
    y = []
    ejeXbin = [nrziCode[0]]

    if nrziCode[0] == '0':
        y.append(bipolar)
    else:
        y.append(int(nrziCode[0]))

    for i in range(1,len(nrziCode)):    
        
        if nrziCode[i] == nrziCode[i-1]:
            temp = x[-1]
            x.append(temp + 1)
            ejeXbin.append(nrziCode[i])
            
        else:
            temp = x[-1]
            x.append(temp)
            x.append(temp+1)
            ejeXbin.append('')
            ejeXbin.append(nrziCode[i])

    for i in range(1,len(nrziCode)):
        if nrziCode[i] == nrziCode[i-1]:
            #print("i:",i)
            temp = y[-1]
            y.append(temp) 
            
        else:
            temp = y[-1]
            if temp == bipolar:
                y.append(temp)
                y.append(1)
            elif temp == 1:
                y.append(temp)
                y.append(bipolar)           
            
    y.append(y[-1])
    ejeXbin.append(ejeXbin[-1])

    if len(x) == len(y): #este if conpara si lo nrziCodes ingresados estan en pares ordenados, si no estan en pares ordenados, entonces no grafica, esto para evitar que se detenga el programa completamente pero funcione el resto
        plt.axhline(0,0,1,c= 'k')# crea el formato de la linea que representa los pares ordenados
        plt.plot(x,y)   #utiliza los pares ordenados en x y y para ir colocando la linea de grafico
        
        plt.xticks(x, ejeXbin, rotation ='horizontal') #coloca las etiquetas de 0 o 1 en el eje x
        
        plt.title("Forma de señal NRZI") #titulo del grafico
        plt.show()  #muestra el grafico
    else:
        print("Error interno, no se puede graficar porque la cantidad de nrziCodes de x y de y son distitos")


root.mainloop()
