import string
import math
import numpy as np
import sympy as sp

#Diccionario empieza en " ", contiene ñ y termina en "."
diccionario=list(string.ascii_uppercase)
diccionario.insert(14,"Ñ")
diccionario.insert(0," ")
diccionario.append(".")

#Hacer + dinamico luego, tipo poder pedir el tamaño de la matriz. 
#El punto es solo q la matriz clave sea invertible entonces solo habria que testearla si se genera random.
key=np.array([[1,2,1,],
               [0,-1,3],
               [2,1,0]])
keysize=len(key)

## .upper por que el diccionario esta todo en mayusculas y hace mas facil la comparacion.
omessage=(input("Ingrese el mensaje a codificar: ")).upper()


## crea una matriz con el mismo numero de columnas que la matriz clave
def tomatriz(omessage, keysize): 
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

    
print(tomatriz(omessage,keysize))



# if __name__ == "__main__":
#     main()