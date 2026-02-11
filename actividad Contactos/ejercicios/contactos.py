def registro():
    #solicitar identificación
    ID = input(f"Ingrese su numero de identificación: ")
    #solicitar nombre
    Nombre = input(f"Ingrese su Nombre: ")
    #solicitar apellido
    Apellido = input(f"Ingrese su apellido: ")
    #solicitar genero
    genero = input(f"Ingrese su genero: ")
    #solicitar correo
    correo = input(f"Ingrese su correo electronico: ")  
    try:
        with open("Datos\contactos.txt", "a") as archivo:
            archivo.write(f"{ID}, {Nombre}, {Apellido}, {genero}, {correo}\n")
            print("Contacto registrado exitosamente.")
            archivo.close()
    except IOError:
        print("Error al registrar el contacto.")
    
    return(ID, Nombre, Apellido, genero, correo)

def consulta():
    #Consultar por identificación
    input_ID = input(f"Ingrese el numero de identificación a consultar: ") 
    bandera = False 
    try:
        with open("Datos\contactos.txt", "r") as archivo:
            contactos= archivo.readlines()
            for contacto in contactos:
                Datos = contacto.strip().split(", ")
                if input_ID in Datos[0]:
                    print("Contacto encontrado:")
                    print(f"{Datos[0]}, {Datos[1]}, {Datos[2]}, {Datos[3]}, {Datos[4]}")
                    bandera = True
                    break
            if not bandera:
                print("Contacto no encontrado.")  
            archivo.close()
    except IOError:
        print("Error al leer el archivo de contactos.")
    return()

def listar():
    #Listar contactos
    try:
        with open("Datos\contactos.txt", "r") as archivo:
            contactos = archivo.readlines()
            for contacto in contactos:
                print(contacto.strip())
            archivo.close()
    except IOError:
        print("Error al leer el archivo de contactos.")
    return()
# Crear archivo de contactos
try:
    with open("Datos\contactos.txt", "x") as archivo:
        archivo.write("ID, Nombre, Apellido, Genero, Correo\n")
        print("Tabla de contactos creada exitosamente.")
        print("Archivo creado exitosamente.")
        archivo.close()
except IOError:
    print("Error al crear el archivo.")
    
#Mostrar menu 
opcion=0
while opcion != 4:
    print("===============================")
    print("     Gestion de Contactos      ")
    print(" 1. Agregar                    ")
    print(" 2. Consultar por ID           ")
    print(" 3. Listar contactos           ")
    print(" 4. Salir                      ") 
    print("===============================")
    print("Ingrese opcion: ",end=" ")
    opcion = int(input())
    
    match opcion:
        case 1:
            print("Registro de contacto:")
            registro()
        case 2:
            print("Consulta por ID:")
            consulta()
        case 3:
            print("Lista de contactos:")
            listar()
        case 4:
            print("Saliendo del sistema...")