import string, math, random
import numpy as np
import sympy as sp
import time

#Diccionario empieza en " ", contiene ñ y termina en "."
diccionario=list(string.ascii_uppercase)
diccionario.insert(14,"Ñ")
diccionario.insert(0," ")
diccionario.append(".")

## crea una matriz con el mismo numero de columnas que la matriz clave
def toMatriz(omessage, keysize): 
    message_matriz=np.zeros((keysize,keysize))
    row=[]
    k=0
    ## math.ceil es para round up la division
    for i in range(math.ceil(len(omessage)/keysize)):
        subrow=[]
        for j in range(keysize):
            try:
                num=diccionario.index(omessage[j+k])
                subrow.append(num)
            except:
                ## cuando se acabe el mensaje, se completa la row incompleta con 0's pues serian espacios en blanco
                subrow.append(0)
        k+=(keysize)
        row.append(subrow)
    message_matriz=np.array(row)
    return message_matriz

## matriz fila para guardar temporalmente cada fila del mensaje ingresado
temporalRow = []
## matriz que guarda el mensaje encriptado
encodeMessage = []

# función para encriptar
def encode(message_matriz,key):
    ## for para recorrer la matriz con el mensaje ingresado y encriptarlo 
    for row in range(len(message_matriz)):
        temporalRow = message_matriz[row]
        encodeMessage.append(np.matmul(temporalRow, key))
        temporalRow = []
    return encodeMessage

# función para imprimir el mensaje encriptado
def prettyPrint(encodeMessage):
    for i in encodeMessage:
        for j in i:
            print(j, end=" ")


def toDictionary(encodeMessage):
    msg = ""
    for i in encodeMessage:
        for j in i:
            letra = diccionario[int(j)%len(diccionario)]
            msg = msg + letra
    return msg

def toMatrix(message, keysize): 
    mess = list(map(int, message.split()))
    message_matriz=np.zeros((math.ceil(len(mess)/keysize),keysize))
    row=[]
    rows = 0
    k=0
    while rows < (math.ceil(len(mess)/keysize)):
        subrow=[]
        for j in range(keysize):    
            try:
                num = mess[j+k]
                subrow.append(num)
            except:
                subrow.append(0)
        k += keysize
        row.append(subrow)
        message_matriz=np.array(row)
        rows += 1
    return message_matriz

#funcion para convertir matriz secreta a letras.
def toMOD_Dictionary(encodeMessage,mod_for_encryption):
    msg = ""
    # print("TERMINA EN "+diccionario[10])
    # print("MOD EMPIEZA EN "+diccionario[11])
    for i in encodeMessage:
        for j in i:
            ## la variable c representa la cantidad de veces q el numero es divisible en el mod. 
            ## Esto servira para despues poder regresar las letras a la matriz codificada.
            c=11      
            for times in range(math.floor(j/mod_for_encryption)): 
                c+=1
            # print(j,", MOD = "+str((int(j)%11)),",times = "+str(c-11)+",C = "+str(c))
            # print("j/11="+str(math.floor(j/11)))
            ## mod 11. La matriz encodeMessage estara letras de _ hasta J
            letra=diccionario[int(j)%mod_for_encryption]+diccionario[c]
            msg = msg + letra
    return msg

# funcion para convertir letras en MOD devuelta a string de numeros que conforman matriz
def FromSecretMessage_to_OriginalNumbers(secretmessage,mod_for_encryption):
    original_numbers=""
    for i in range(len(secretmessage)):
        ## i debe ser multiplo de 2 pues las pares son letras y las impares son el mod
        if (i%2==0):
            l=secretmessage[i]
            mod_l=secretmessage[i+1]

            number=diccionario.index(l)
            mod_number=diccionario.index(mod_l)

            mod_number=mod_number-mod_for_encryption

            originalnumber=number+(mod_number*mod_for_encryption)
            original_numbers=original_numbers+" "+str(originalnumber)

    return original_numbers


# función para desencriptar
def decode(message, keyInv):
    invKey = np.linalg.inv(keyInv)
    result = np.matmul(message,invKey)
    result = np.round(result, 5)
    return result


            

# función para leer un archivo
def Leerfile(filename):
    file= open(filename, mode = 'r') 
    texto_s = file.read()
    return texto_s

# función para crear y escribir un archivo
def EscribirFile(message):
    Time = str(time.strftime("%H:%M:%S"))
    date = str(time.strftime("%d-%m-%y"))
    fileName = "msgEncriptado(" + date + "_" + Time + ").txt"
    print("Nombre del archivo: " + fileName)

    file = open(fileName, mode = "w") 
    file.write(message)
    file.close()
