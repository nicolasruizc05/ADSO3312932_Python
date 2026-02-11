"""
with open("salida.txt","a") as archivo:
    archivo.write("Hola mundo desde python \n")
    archivo.write("Manejo de archivos de Texto \n")
archivo.close()

try:
    with open("salida.txt","a",encoding="UTF-8") as archivo:
        archivo.write("Hola mundo desde python \n")
        archivo.write("Manejo de archivos de Texto misión SENA \n")
    archivo.close()
except IOError as error:
    print(str(error))
"""    
# crear un archivo sin borrar si ya existe
    
try:
    with open("salida.txt","x",encoding="UTF-8") as archivo:
        archivo.write("Hola mundo desde python \n")
        archivo.write("Manejo de archivos de Texto misión SENA \n")
    archivo.close()
except IOError as error:
    print(str(error))
    