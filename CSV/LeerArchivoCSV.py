import csv
with open('personas.csv',newline='', encoding= "utf-8") as archivo:
     lector= csv.reader(archivo) #Cada dato de la fila se convierte en una lista
     print(type(lector))
    
     for fila in lector:
        print(fila,"\t")
        
        
# Leer archivos usando diccionarios

with open("personas.csv", newline="",encoding="utf-8") as archivo:
    lector=csv.DictReader(archivo)
    
    for fila in lector:
        print("  ")
        # print(fila)
        print(f"Nombre:\t {fila['nombre']}")
        print(f"Edad:\t {fila['edad']}")
        print(f"Ciudad:\t {fila['ciudad']}")
        print("*" *20)
    
    