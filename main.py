import random
import numpy as np
import codificar as cod

## main
def main():
    keysize = random.randint(3,5)
    keyValue = random.randint(3,5)
    key = np.random.randint((keyValue), size=(keysize, keysize))

    print("\n\n--------------- PROYECTO CRIPTOGRAFÍA ---------------")

    print("\n1. Encriptar un archivo .txt ")
    print("2. Encriptar un mesaje ")
    print("3. Desencriptar y generar un archivo .txt ")
    print("4. Desencriptar un mensaje ")
    
    seguir = "y"

    while seguir == "y":
        opcion = int(input("\n► Ingrese el número correspondiente a la accion que desea realizar: "))
        
        if opcion == 1:
            print("\n\n////////// ENCRIPTANDO ARCHIVO //////////")

            filename = input("\n► Ingrese el nombre del archivo .txt a encriptar: ")
            omessage = (cod.Leerfile(filename)).upper()   # ingreso por archivo .txt

            ToMatrix = cod.toMatriz(omessage, keysize)
            encodeMessage = cod.encode(ToMatrix, key)
            
            print("\n\n• Mensaje encriptado:")
            cod.prettyPrint(encodeMessage)

            print("\n\n• Matriz clave: ")
            cod.prettyPrint(key)

            print("\n\n• Tamaño clave: \n", keysize)

            print("\n/////////////////////////////////////////")

        if opcion == 2:
            print("\n\n////////// ENCRIPTANDO MENSAJE //////////")

            omessage = input("\n► Ingrese el mensaje a encriptar: ").upper() # ingreso manual

            ToMatrix = cod.toMatriz(omessage,keysize)
            encodeMessage = cod.encode(ToMatrix, key)

            print("\n\n• Mensaje encriptado:")
            # toDictionary(encodeMessage)
            cod.prettyPrint(encodeMessage)

            print("\n\n• Matriz clave: ")
            cod.prettyPrint(key)

            print("\n\n• Tamaño clave: \n", keysize)

            print("\n/////////////////////////////////////////")

        if opcion == 3:
            print("\n\n////////// DESENCRIPTADNO //////////")

            message = (input("\n► Ingrese el mensaje a desencriptar: ")).upper()
            keyInv = input("\n► Ingrese la matriz clave: ")
            keysize = int(input("\n► Ingrese el tamaño de la matriz clave: "))
            print("")

            print("\n----- Se ha creado el archivo exitosamente -----\n")
            message = cod.toMatrix(message, keysize)
            keyInv = cod.toMatrix(keyInv,keysize)
            msg = str(cod.toDictionary(cod.decode(message, keyInv)))

            cod.EscribirFile(msg)

            print("\n//////////////////////////////////////")

        
        if opcion == 4:
            print("\n\n////////// DESENCRIPTADNO //////////")

            message = (input("\n► Ingrese el mensaje a desencriptar: ")).upper()
            keyInv = input("\n► Ingrese la matriz clave: ")
            keysize = int(input("\n► Ingrese el tamaño de la matriz clave: "))
            print("")

            print("\n----- Mensaje desencriptado -----\n")
            message = cod.toMatrix(message, keysize)
            keyInv = cod.toMatrix(keyInv,keysize)
            print(cod.toDictionary(cod.decode(message, keyInv)))
            print("")

            print("\n//////////////////////////////////////")

        seguir = input("\n\n► ¿Desea realizar otra acción? (y/n): ")



if __name__ == "__main__":
    main()