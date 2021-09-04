from tkinter import *

par=int(input("Presione 1 para paridad par y 0 para impar: "))

##Insertar los bits de paridad en la secuencia de bits

bits = [1,0,1,0,0,1,0,1,1,1,0,1]
print("Estos son los bits NRZI")
print(bits)
bits.insert(0,0)
bits.insert(1,0)
bits.insert(3,0)
bits.insert(7,0)
bits.insert(15,0)
#print(bits)

##Posiciones a examinar
p1=[2,4,6,8,10,12,14,16]
p2=[2,5,6,9,10,13,14]
p3=[4,5,6,11,12,13,14]
p4=[8,9,10,11,12,13,14]
p5=[16]
hbits=[p1,p2,p3,p4,p5]

p1e=[0,2,4,6,8,10,12,14,16]
p2e=[1,2,5,6,9,10,13,14]
p3e=[3,4,5,6,11,12,13,14]
p4e=[7,8,9,10,11,12,13,14]
p5e=[15,16]
hbitse=[p1e,p2e,p3e,p4e,p5e]
ones=0
parpos=0
n=0
for a in hbits:
    ones=0
    n=n+1
    for i in a:
        ones=bits[i]+ones

    if par==0:
        if (ones%2)!=0:
            bits[parpos]=1
    if par==1:
        if (ones%2)==0:
            bits[parpos]=1
    parpos = 2**n-1
if par==1:
    hola="par"
else:
    hola="impar"
print("Estos son los valores de los bits con la paridad " + hola + ".")
print(bits)

####################################################################################################
def root1(bits):
    izquierda=["Sin paridad","p1","p2","p3","p4","p5","Con paridad"]
    n=1
    for i in izquierda:
        x = Label(root, text=i).grid(row=n, column=0)
        n+=1
    denominacion=["","p1","p2","d1","p3","d2","d3", "d4", "p4","d5","d6","d7","d8","d9","d10","d11","p5","d12"]
    n=1
    for i in denominacion:
        x = Label(root, text=i).grid(row=0, column=n)
        n+=1

    n=2
    for i in bits:
        l = Label(root, text=i).grid(row=7, column=n)
        n+=1

    numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pos=0
    poxx=2
    n=2
    xx=0

    for h in hbitse:
        for i in numeros:
            if i in h:
                x = Label(root, text=bits[i]).grid(row=poxx, column=n)
            else:
                x = Label(root, text="").grid(row=poxx, column=n)
            n += 1
            xx += 1
        n=2
        poxx+=1

    sin_paridad=[2,4,5,6,8,9,10,11,12,13,14,16]
    for i in numeros:
        if i in sin_paridad:
            x = Label(root, text=bits[i]).grid(row=1, column=n)
        else:
            x = Label(root, text="").grid(row=1, column=n)
        n += 1
        xx += 1
root.mainloop()

####################################################################################################

##detectando errores y estableciendo con cual bit de paridad es
##Posiciones para detectar errores
#print(bits)
##fp es el flag para la posicion en hbits del bit de paridad con el que hay error
bits2=bits
map=[2,4,5,6,8,9,10,11,12,13,14,16]
error=int(input("Introduzca la posicion de bit de informacion que desea cambiar (del 1 al 12): "))
error=error-1
if bits2[map[error]]==0:
    bits2[map[error]]=1
else:
    bits2[map[error]]=0
#print(bits)
print("Estos son los bits con el cambio de bit en la posición " + str(error+1) + ".")
print(bits2)
#print("antes del chekeo")

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
#print(fp)
##fp es el numero binario de la posicion del 1-17 en el que se encuentra el error

####################################################################################################

##Segunda parte##

root = Tk()
root.title("Comprobación de bits de paridad")
izquierda=["Recibido","p1","p2","p3","p4","p5"]
denominacion=["","p1","p2","d1","p3","d2","d3", "d4", "p4","d5","d6","d7","d8","d9","d10","d11","p5","d12","Prueba de Paridad","Bit de paridad"]

n=1
for i in izquierda:
    x = Label(root, text=i).grid(row=n, column=0)
    n+=1

n=1
for i in denominacion:
    x = Label(root, text=i).grid(row=0, column=n)
    n+=1

bits2=[1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1]
n=2
for i in bits2:
    l = Label(root, text=i).grid(row=1, column=n)
    n+=1

pos=0
poxx=2
n=2
xx=0

for h in hbitse:
    for i in numeros:
        if i in h:
            x = Label(root, text=bits2[i]).grid(row=poxx, column=n)
        else:
            x = Label(root, text="").grid(row=poxx, column=n)
        n += 1
        xx += 1
    n=2
    poxx+=1
poxx=2

for i in fp:
    if i == 0:
        x = Label(root, text="Correcto").grid(row=poxx, column=19)
        xx = Label(root, text=i).grid(row=poxx, column=20)
    else:
        y = Label(root, text="Error").grid(row=poxx, column=19)
        y = Label(root, text=i).grid(row=poxx, column=20)
    poxx+=1
root.mainloop()

####################################################################################################

otro=input("Desea cambiar otra posición? (1:sí, 2:no)")
while otro == 1:
    bits2 = bits
    map = [2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16]
    error = int(input("Introduzca la posicion de bit de informacion que desea cambiar (del 1 al 12): "))
    error = error - 1
    if bits2[map[error]] == 0:
        bits2[map[error]] = 1
    else:
        bits2[map[error]] = 0
    print(bits)
    print(bits2)