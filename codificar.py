import string
import numpy as np
import sympy as sp


diccionario=list(string.ascii_uppercase)
diccionario.insert(0," ")
#El diccionario no contiene Ñ

omessage=input("Ingrese el mensaje a codificar: ")
print(omessage)
#Hacer + dinamico luego, tipo poder pedir el tamaño de la matriz. 
#El punto es solo q la matriz clave sea invertible entonces solo habria que testearla si se genera random.
key=np.array([[1,2,1,],
               [0,-1,3],
               [2,1,0]])


# if __name__ == "__main__":
#     main()