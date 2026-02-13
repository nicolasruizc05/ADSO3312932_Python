import csv

codigo=int(input("Ingrese codigo del producto a agregar"))
nombre=input("Ingrese nombre de producto a agregar")
precio=int(input("Ingrese precio del producto"))
categoria=input("Ingrese la categoria del producto")

nuevoproducto=[codigo,nombre,precio,categoria]
try:
    with open("productos.csv","a",newline='',encoding="Utf-8") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(nuevoproducto)
        print("Producto agregado exitosamente")
except IOError as error:
    print(str(error))
    