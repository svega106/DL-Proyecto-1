dato = ""
def ingDato():   

    cuatro = False
    octal = False

    while octal == False:
 
        dato = input("Digite un numero Octal de 4 digitos :")
        oct = 0

        #Determinar si es de 4 digitos
        if len(dato) > 4:

            print("El número ingresado tiene mas de 4 digitos, favor ingresar otro numero")
        else:
            cuatro = True
            
        if cuatro == True:
        #Determinar si es numero Octal    
            for i in dato:
                if i >= "8":
                    oct =+ 1
            if oct != 0:
                print("Numero NO es Octal, favor ingrese otro numero")
            else:
                octal = True
                n10 = octToDec(dato)
                datoBin = octToBin(n10) #Llama la función que convierte a binario. Esa función recibe el dato en decimal y lo devuelve de tipo bin
                octToHex(n10) #Llama la función que convierte a hexadecimal. Esa función recibe el dato en decimal y lo devuelve de tipo hex
                nrzi(datoBin) #Llama la funcion que hace la conversión a codigo nrzi    
    
    
#Pasar numero octal a base 10
def octToDec(dato):
    n10 = 0 #Variable donde se va a almacenar el dato convertido a decimal

    for i in range(0,len(dato)):
        n10 += int(dato[len(dato)-1-i])*pow(8,i) #recorre el dato y hace lo necesario para convertirlo a decimal

    print("Numer en Decimal :", n10)
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

    print("Numero en Binario :", n2)
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

    print ("Numero en Hexadecimal :",nhex)
    
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
    print("Codigo NRZI:",nrziCode)
    return nrziCode

def dif(d):#funcion que devuelve el caracter contrario a otro caracter

    x = str(d)
    if x == '1':
        return str(0)
    elif x == '0':
        return str(1)
    
ingDato()
