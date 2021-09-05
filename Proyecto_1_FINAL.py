import tkinter as tk
from tkinter import *   
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog, Text
import numpy as np
import matplotlib.pyplot as plt

root = Tk()

par = 0

root.title("Proyecto 1 de Diseño Lógico")

#Ingresar texto y calcular
tit = Label(root, text= "Favor ingresar un numero octal de 4 digitos unicamente")
tit.grid(row=0, column=0, columnspan = 3)

num = Entry(root, width=45, borderwidth=5)
num.grid(row = 1, column = 0 , columnspan = 1, padx = 10, pady = 10)

cal = Button(root, text="Calcular",command = lambda:ingDato(num.get()))
cal.grid(row = 1, column = 2)

def segundaParte():
    tit2 = Label(root, text = "Codificacion NRZI")
    tit2.grid(row = 5, column = 0, columnspan = 3)
    nr = Label(root, text = nrzi(octToBin(octToDec(num.get()))))
    nr.grid(row = 6, column = 0, columnspan = 2)
    nrzbut = Button(root, text = "Generar grafica de NRZI", command = lambda:crearGrafico(nrzi(octToBin(octToDec(num.get())))))
    nrzbut.grid(row = 6, column = 1)

    nrz = nrzi(octToBin(octToDec(num.get())))
    bits = []
    for i in nrz:
        bits.append(int(i))

    extra = Label(root, text = "")
    extra.grid(row = 8, column = 0, columnspan = 3)

    paridadtit = Label(root, text = "Elija el tipo de Paridad")
    paridadtit.grid(row = 9, column = 0, columnspan = 2)

    paridadpar = Button(root, text = "Paridad Par", command = lambda:paridad(1))
    paridadpar.grid( row = 9, column = 2)

    paridadimpar = Button(root, text = "Paridad Impar",command = lambda:paridad(0))
    paridadimpar.grid( row = 9, column = 3)

    def paridad(pari):
        bits2 = []
        bits2 = bits

        par = pari
        paridadtit = Label(root, text = par)
        paridadtit.grid(row = 10, column = 0, columnspan = 2)

        if len(bits2) == 17:
            posicionesparidad = [0,1,3,7,15]
            for i in posicionesparidad:
                bits[i] = 0
        
        else:
            bits2.insert(0,0)
            bits2.insert(1,0)
            bits2.insert(3,0)
            bits2.insert(7,0)
            bits2.insert(15,0)

        ##Posiciones a examinar
        p1=[2,4,6,8,10,12,14,16]
        p2=[2,5,6,9,10,13,14]
        p3=[4,5,6,11,12,13,14]
        p4=[8,9,10,11,12,13,14]
        p5=[16]
        hbits=[p1,p2,p3,p4,p5]
        
        ones=0
        parpos=0
        n=0
        for a in hbits:
            ones=0
            n=n+1
            for i in a:
                ones=bits2[i]+ones

            if par==0:
                if (ones%2)!=0:
                    bits2[parpos]=1
            if par==1:
                if (ones%2) ==0:
                    bits2[parpos]=1
            parpos = 2**n-1
        if par==1:
            hola="par"
        else:
            hola="impar"
        texto = Label(root, text = "Estos son los valores de los bits con la paridad " + hola + ".")
        texto.grid(row = 10,column = 0)
        bitsprint = Label(root, text = bits2)
        bitsprint.grid(row = 10, column = 1)

        tablaparidad = Button(root, text = "Mostrar Tabla de Paridad", command = lambda:root1(bits2,par))
        tablaparidad.grid(row = 11, column = 0)



def root1(bits2,par):
    newWindow1 = Toplevel(root)
    newWindow1.title("Tabla de Paridad")

    p1e=[0,2,4,6,8,10,12,14,16]
    p2e=[1,2,5,6,9,10,13,14]
    p3e=[3,4,5,6,11,12,13,14]
    p4e=[7,8,9,10,11,12,13,14]
    p5e=[15,16]

    hbitse=[p1e,p2e,p3e,p4e,p5e]

    izquierda=["Sin paridad","p1","p2","p3","p4","p5","Con paridad"]
    n=1
    for i in izquierda:
        x = Label(newWindow1, text=i).grid(row=n, column=0)
        n+=1
    denominacion=["","p1","p2","d1","p3","d2","d3", "d4", "p4","d5","d6","d7","d8","d9","d10","d11","p5","d12"]
    n=1
    for i in denominacion:
        x = Label(newWindow1, text=i).grid(row=0, column=n)
        n+=1

    n=2
    for i in bits2:
        l = Label(newWindow1, text=i).grid(row=7, column=n)
        n+=1

    numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pos=0
    poxx=2
    n=2
    xx=0

    for h in hbitse:
        for i in numeros:
            if i in h:
                x = Label(newWindow1, text=bits2[i]).grid(row=poxx, column=n)
            else:
                x = Label(newWindow1, text="").grid(row=poxx, column=n)
            n += 1
            xx += 1
        n=2
        poxx+=1

    sin_paridad=[2,4,5,6,8,9,10,11,12,13,14,16]
    for i in numeros:
        if i in sin_paridad:
            x = Label(newWindow1, text=bits2[i]).grid(row=1, column=n)
        else:
            x = Label(newWindow1, text="").grid(row=1, column=n)
        n += 1
        xx += 1

    clicked = IntVar()
    clicked.set(1)

    title = Label(root, text = "Cual bit quiere cambiar?")
    title.grid(row = 12, column = 0)

    dropdown = OptionMenu(root, clicked, 1,2,3,4,5,6,7,8,9,10,11,12)
    dropdown.grid(row = 12, column = 1)


    tablaerror = Button(root, text = "Mostrar Tabla de Error con bit cambiado", command = lambda:error())
    tablaerror.grid(row = 12, column = 2 )


    def error():
        map=[2,4,5,6,8,9,10,11,12,13,14,16]

        error=clicked.get()
        error=error-1
        if bits2[map[error]]==0:
            bits2[map[error]]=1
        else:
            bits2[map[error]]=0

        
        bitsprint = Label(root, text = "Estos son los bits con el cambio de bit en la posición " + str(error+1) + ".")
        bitsprint.grid(row = 13, column = 0)
        printbits = Label(root, text = bits2)
        printbits.grid(row = 13, column = 2)

        fp=[0,0,0,0,0]
        ones=0
        fpi=0
        for a in hbitse:
            ones = 0
            for i in a:
                ones=bits2[i]+ones
            if par==0:
                if (ones % 2) != 0:
                    fp[fpi]=1
            if par==1:
                if (ones % 2) == 0:
                    fp[fpi]=1
            fpi=fpi+1

        #if par == 1:
           # for i in range(fp):
              #  if fp[i] == 1:
             #       fp[i] = 0
              #  else:
               #     fp[i] = 1

        
        newWindow2 = Toplevel(root)
        newWindow2.title("Tabla de paridad con error")

        izquierda=["Recibido","p1","p2","p3","p4","p5"]
        denominacion=["","p1","p2","d1","p3","d2","d3", "d4", "p4","d5","d6","d7","d8","d9","d10","d11","p5","d12","Prueba de Paridad","Bit de paridad"]

        n=1
        for i in izquierda:
            x = Label(newWindow2, text=i).grid(row=n, column=0)
            n+=1

        n=1
        for i in denominacion:
            x = Label(newWindow2, text=i).grid(row=0, column=n)
            n+=1

        n=2
        for i in bits2:
            l = Label(newWindow2, text=i).grid(row=1, column=n)
            n+=1

        pos=0
        poxx=2
        n=2
        xx=0

        for h in hbitse:
            for i in numeros:
                if i in h:
                    x = Label(newWindow2, text=bits2[i]).grid(row=poxx, column=n)
                else:
                    x = Label(newWindow2, text="").grid(row=poxx, column=n)
                n += 1
                xx += 1
            n=2
            poxx+=1
        poxx=2

        for i in fp:
            if i == 0:
                x = Label(newWindow2, text="Correcto").grid(row=poxx, column=19)
                xx = Label(newWindow2, text=i).grid(row=poxx, column=20)
            else:
                y = Label(newWindow2, text="Error").grid(row=poxx, column=19)
                y = Label(newWindow2, text=i).grid(row=poxx, column=20)
            poxx+=1    



    

    



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

#Crea el codigo NRZI
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

#funcion que devuelve el caracter contrario a otro caracter
def dif(d):

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
