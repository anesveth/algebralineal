import codificar as cod
import numpy as np
import sympy as sp

# Inversa matriz clave
key_inv = np.linalg.inv(cod.key)
message = [24, 9, 42, 27, 22, 68, 10, 11, 4, 52, 43, 15, 52, 37, 77, 72, 47, 55]

def decode(message):
    cont = 0
    ops = len(message) / len(key_inv)
    while cont < ops:
        numb = []
        for i in range(len(key_inv)):
            numb.append(message[i])
        for i in numb:
            message.remove(i)
        result = np.dot(numb,key_inv)
        print(result)
        cont += 1

