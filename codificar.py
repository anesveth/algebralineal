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

def toDictionary(encodeMessage):
    msg = ""
    for i in encodeMessage:
        for j in i:
            letra = diccionario[int(j)%len(diccionario)]
            msg = msg + letra
    return msg
            
# función para imprimir el mensaje encriptado
def prettyPrint(encodeMessage):
    for i in encodeMessage:
        for j in i:
            print(j, end=" ")

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
    print("Nombre del archivo es: " + fileName)

    file = open(fileName, mode = "w") 
    file.write(message)
    file.close()
