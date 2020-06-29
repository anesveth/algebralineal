import string
import math
import random
import numpy as np
import sympy as sp

#Diccionario empieza en " ", contiene ñ y termina en "."
diccionario=list(string.ascii_uppercase)
diccionario.insert(14,"Ñ")
diccionario.insert(0," ")
diccionario.append(".")

#Hacer + dinamico luego, tipo poder pedir el tamaño de la matriz. 
#El punto es solo q la matriz clave sea invertible entonces solo habria que testearla si se genera random.
#key=np.array([[1,2,1,],
                #[0,-1,3],
                #[2,1,0]])
#keysize = len(key)
keysize = random.randint(3,5)
keyValue = random.randint(3,5)
key = np.random.randint((keyValue), size=(keysize, keysize))

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

def encode(message_matriz,key):
    ## for para recorrer la matriz con el mensaje ingresado y encriptarlo 
    for row in range(len(message_matriz)):
        temporalRow = message_matriz[row]
        encodeMessage.append(np.matmul(temporalRow, key))
        temporalRow = []

def toDictionary(encodeMessage):
    for i in encodeMessage:
        # for j in i:
            ## mod en length del diccionario para que calzen todos los numeros dentro del diccionario
        print(diccionario[int(i)%len(diccionario)],end=" ")
            
def prettyPrint(encodeMessage):
    for i in encodeMessage:
        for j in i:
            print(j, end=" ")

key_inv = np.linalg.inv(key) # se deben ingresar

def decode(message):
    cont = 0
    ops = len(message) / len(key_inv)
    deco = ""
    while cont < ops:
        numb = []
        for i in range(len(key_inv)):
            numb.append(message[i])
        for i in numb:
            message.remove(i)
        result = np.dot(numb,key_inv)
        result = result.astype(int)
        for i in result:
            deco = deco + str(i) + " "
        cont += 1
    return deco

def Leerfile(filename):
    file= open(filename, mode = 'r') 
    texto_s = file.read()
    return texto_s


## main
def main():
    print("\n\n--------------- PROYECTO CRIPTOGRAFÍA ---------------")
    filename=input("\n--> Ingrese el nombre del file a encriptar: ")
    omessage=(Leerfile(filename)).upper()
    ## Pedir el mensaje
    ## .upper por que el diccionario esta todo en mayusculas y hace mas facil la comparacion.
    #omessage=(input("\n--> Ingrese el mensaje a encriptar: ")).upper()
    print(omessage)
    ## Convertir el mensaje a matriz
    ToMatrix = toMatriz(omessage,keysize)
 
    ## Encriptar mensaje
    encode(ToMatrix, key)
    
    ## Imprimir el mensaje encriptado
    print("\n\n--> Mensaje encriptado:")
    # toDictionary(encodeMessage)
    prettyPrint(encodeMessage)
    print("\n\n")

    message = input("Ingrese el mensaje a decodificar: ")
    # message = message.split()
    mmess = list(map(int, message.split()))
    print(decode(mmess))


if __name__ == "__main__":
    main()