##Insertar los bits de paridad en la secuencia de bits

bits = [1,0,1,0,0,1,0,1,1,1,0,1]

bits.insert(0,0)
bits.insert(1,0)
bits.insert(3,0)
bits.insert(7,0)
bits.insert(15,0)
print(bits)

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
        ones=bits[i]+ones

    if (ones%2)!=0:
        bits[parpos]=1
    parpos = 2**n-1
print(bits)

##detectando errores y estableciendo con cual bit de paridad es
##Posiciones para detectar errores
p1e=[0,2,4,6,8,10,12,14,16]
p2e=[1,2,5,6,9,10,13,14]
p3e=[3,4,5,6,11,12,13,14]
p4e=[7,8,9,10,11,12,13,14]
p5e=[15,16]
print(bits)
##fp es el flag para la posicion en hbits del bit de paridad con el que hay error
bits[5]=0
print("antes del chekeo",bits)
fp=[0,0,0,0,0]
hbits=[p1e,p2e,p3e,p4e,p5e]
ones=0
fpi=0
for a in hbits:
    ones = 0
    for i in a:
        ones=bits[i]+ones
    if (ones % 2) != 0:
       fp[fpi]=1
    fpi=fpi+1
print(fp)
##fp es el numero binario de la posicion del 1-17 en el que se encuentra el error