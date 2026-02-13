import csv

datos=[
    ["codigo","nombre","precio","categoria"],
    [10,"Televisor",2500000,"Electrodomestico"],
    [11,"Tenis",390000,"Calzado"],
    [12,"Chaqueta",420000,"Ropa"],
    [13,"Nevera",3400000,"Electrodomestico"]
]

with open("productos.csv", "w",newline='',encoding="utf-8") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(datos)