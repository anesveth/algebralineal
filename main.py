import random
import numpy as np
import codificar as cod

## main
def main():
    keysize = random.randint(3,5)
    keyValue = random.randint(3,5)
    key = np.random.randint((keyValue), size=(keysize, keysize))

    print("\n\n--------------- PROYECTO CRIPTOGRAFÍA ---------------")
    print("\nQué desea hacer?")
    print("1. Encriptar un archivo .txt ")
    print("2. Encriptar un mesaje ")
    print("3. Desencriptar y generar un archivo .txt ")
    print("4. Desencriptar un mensaje ")
    
    seguir = "y"

    while seguir == "y":
        opcion = int(input("\nIngrese el número de la accion que desea realizar: "))
        
        if opcion == 1:
            filename=input("\n--> Ingrese el nombre del archivo .txt a encriptar: ")
            omessage = (cod.Leerfile(filename)).upper()   # ingreso por archivo .txt

            ToMatrix = cod.toMatriz(omessage, keysize)
            encodeMessage = cod.encode(ToMatrix, key)
            
            print("\n\n--> Mensaje encriptado:")
            cod.prettyPrint(encodeMessage)
            print("\n--> Matriz clave: ")
            cod.prettyPrint(key)
            print("\n--> Tamaño clave:", keysize)
            print("\n\n")

        if opcion == 2:
            omessage = input("\n--> Ingrese el mensaje a encriptar: ").upper() # ingreso manual

            ToMatrix = cod.toMatriz(omessage,keysize)
            encodeMessage = cod.encode(ToMatrix, key)

            print("\n\n--> Mensaje encriptado:")
            # toDictionary(encodeMessage)
            cod.prettyPrint(encodeMessage)
            print("\n--> Matriz clave: ")
            cod.prettyPrint(key)
            print("\n\n")
        if opcion == 3:
            pass
        
        if opcion == 4:
            message = (input("\n--> Ingrese el mensaje a decodificar: ")).upper()
            keyInv = input("\n--> Ingrese la matriz clave: ")

            keysize = int(input("--> Ingrese el tamaño de la matriz clave: "))
            print("")
            message = cod.toMatrix(message, keysize)
            keyInv = cod.toMatrix(keyInv,keysize)
            cod.toDictionary(cod.decode(message, keyInv))

        seguir = input("\\nnDesea realizar otra accion? (y/n) ")



if __name__ == "__main__":
    main()