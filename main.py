par=int(input("Presione 1 para paridad par y 0 para impar: "))


bits = [1,0,1,0,0,1,0,1,1,1,0,1]

##Posiciones a examinar para determinar pariedad
p1=[2,4,6,8,10,12,14,16]
p2=[2,5,6,9,10,13,14]
p3=[4,5,6,11,12,13,14]
p4=[8,9,10,11,12,13,14]
p5=[16]
##Mapeo de la posicion nueva de los bits originales
map=[2,4,5,6,8,9,10,11,12,13,14,16]
##Posiciones para detectar errores
p1e=[0,2,4,6,8,10,12,14,16]
p2e=[1,2,5,6,9,10,13,14]
p3e=[3,4,5,6,11,12,13,14]
p4e=[7,8,9,10,11,12,13,14]
p5e=[15,16]

hbits=[p1,p2,p3,p4,p5]
hbitse=[p1e,p2e,p3e,p4e,p5e]

##fp son los flags de errores y dan el numero en binario al reves de la posicion del error del 1 al 17
fp=[0,0,0,0,0]

##Insertar los bits de paridad en la secuencia de bits
def introducirbits(list):
    list.insert(0,0)
    list.insert(1,0)
    list.insert(3,0)
    list.insert(7,0)
    list.insert(15,0)
    return (list)

bits=introducirbits(bits)

def determinarbitspar(list):
    n=0
    parpos=0
    for a in hbits:
        ones=0
        n=n+1
        for i in a:
            ones=list[i]+ones

        if par==0:
            if (ones%2)!=0:
                list[parpos]=1
        if par==1:
            if (ones%2)==0:
                list[parpos]=1
        parpos = 2**n-1
    return(list)

bits=determinarbitspar(bits)

print(bits)
bits2=bits
def introducirerror(list):
    error=int(input("Introduzca la posicion de bit de informacion que desea cambiar (del 1 al 12): "))
    error=error-1
    if list[map[error]]==0:
        list[map[error]]=1
    if list[map[error]]!=0:
        list[map[error]]=0
    return list
bits2=introducirerror(bits2)

print(bits2)
print("antes del chekeo")

##detectando errores y estableciendo con cual bit de paridad es
def detectarerrores(list):
    ones=0
    fpi=0
    for a in hbitse:
        ones = 0
        for i in a:
            ones=bits2[i]+ones
        if par==0:
            if (ones % 2) != 0:
                list[fpi]=1
        if par==1:
            if (ones % 2) == 0:
                list[fpi]=1
        fpi=fpi+1
    return list
fp=detectarerrores(fp)
print(fp)
##fp es el numero binario de la posicion del 1-17 en el que se encuentra el error
print(bits)
