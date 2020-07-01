import string, math, random
import numpy as np
import sympy as sp

#Diccionario empieza en " ", contiene ñ y termina en "."
diccionario=list(string.ascii_uppercase)
diccionario.insert(14,"Ñ")
diccionario.insert(0," ")
diccionario.append(".")

# key=np.array([[1,2,1,],
#                 [0,-1,3],
#                 [2,1,0]])
# keysize = len(key)
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
    return encodeMessage

def toDictionary(encodeMessage):
    for i in encodeMessage:
        for j in i:
            # mod en length del diccionario para que calzen todos los numeros dentro del diccionario
            print(diccionario[int(j)%len(diccionario)],end="")
            
def prettyPrint(encodeMessage):
    for i in encodeMessage:
        for j in i:
            print(j, end=" ")

# crea una matriz con el mismo numero de columnas que la matriz clave
def toMatrix(message, keysize): 
    mess = list(map(int, message.split()))
    message_matriz=np.zeros((math.ceil(len(mess)/keysize),keysize))
    row=[]
    rows = 0
    k=0
    ## math.ceil es para round up la division
    while rows < (math.ceil(len(mess)/keysize)):
        subrow=[]
        for j in range(keysize):    
            try:
                num = mess[j+k]
                subrow.append(num)
            except:
                ## cuando se acabe el mensaje, se completa la row incompleta con 0's pues serian espacios en blanco
                subrow.append(0)
        k += keysize
        row.append(subrow)
        message_matriz=np.array(row)
        rows += 1
    return message_matriz

def decode(message, keyInv):
    invKey = np.linalg.inv(keyInv)
    result = np.matmul(message,invKey)
    result = np.round(result, 5)
    return result

def Leerfile(filename):
    file= open(filename, mode = 'r') 
    texto_s = file.read()
    return texto_s


# ## main
# def main():
#     print("\n\n--------------- PROYECTO CRIPTOGRAFÍA ---------------")
   
#     # filename=input("\n--> Ingrese el nombre del archivo .txt a encriptar: ")
#     # omessage=(Leerfile(filename)).upper()

#     ## Pedir el mensaje
#     ## .upper por que el diccionario esta todo en mayusculas y hace mas facil la comparacion.
#     omessage=(input("\n--> Ingrese el mensaje a encriptar: ")).upper()

#     ## Convertir el mensaje a matriz
#     ToMatrix = toMatriz(omessage,keysize)
 
#     ## Encriptar mensaje
#     encode(ToMatrix, key)
    
#     ## Imprimir el mensaje encriptado
#     print("\n\n--> Mensaje encriptado:")
#     # toDictionary(encodeMessage)
#     prettyPrint(encodeMessage)
#     print("\n\n")

#     message = (input("\n--> Ingrese el mensaje a decodificar: ")).upper()
#     # keyInv = input("\n--> Ingrese la matriz clave: ")
#     keyInv = np.linalg.inv(key) # se deben ingresar
#     keyInvL = len(keyInv)

#     message = toMatrix(message, keyInvL)
#     toDictionary(decode(message, keyInv))



# if __name__ == "__main__":
    # main()