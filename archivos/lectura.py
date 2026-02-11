#Leer un archivo 
"""
try:
    with open("salida.txt","r",encoding="UTF-8") as archivo:
        #texto = archivo.read()  #esto es para leer todo el archivo
        #texto = archivo.readlines() # Muestra todo el texto del archivo pero con formato de lista y muestra el caracter \n
        texto = archivo.readline()
        totalLineas = len(texto)
        print(f"La cantidad de lineas de texto en el archivo es {totalLineas}")
        print(type(texto))
        print(texto)        
    archivo.close
        
except IOError as error:
    print(str(error))
    
"""

# Para leer linea por linea 
lista=[]
try:
    with open("salida.txt","r",encoding="UTF-8") as archivo:
        for linea in archivo:
            #print(linea.strip())
            #print(linea)
            lista.append(linea)
            lista.append(linea.strip())
        archivo.close()
except IOError as error:
    print(str(error))
    
print(lista)