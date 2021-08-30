#Este programa 

cuatro = False
octal = False

while octal == False:

    n = input("Digite un numero Octal de 4 digitos :")

    oct = 0
    #Determinar si es de 4 digitos
    if len(n) > 4:
        print("Numero es mayor a cuatro, favor ingresar otro numero")
    else: 
        cuatro = True

    if cuatro == True:
    #Determinar si es numero Octal    
        for i in n:
            if i >= "8":
                oct =+ 1
        if oct < 1:
            octal = True
        else:
            print("Numero NO es Octal, favor ingrese otro numero")

#Pasar numero octal a base 10
n10 = 0

for i in range(0,len(n)):
    n10 += int(n[len(n)-1-i])*pow(8,i)

print("Numer en Decimal :", n10)

#Convertir numero a Binario
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

print("Numero en Binario :", n2)

#Convertir numero a Hexadecimal 
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

print ("Numero en Hexadecimal :",nhex)