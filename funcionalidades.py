from json import dumps, load

archivo_usuarios = "usuarios.json"
archivo_vehiculos = "vehiculos.json"
archivo_citas = "citas.json"
archivo_instructores = "instructores.json"


#FUNCIONES JSON

def leer_json(archivito):
    respuesta = {}
    with open(archivito, "r") as archivo:
        respuesta = load(archivo)
        return respuesta
    
def escribir_json(archivito, contenido):
    with open(archivito, "w") as archivo:
        guardar = dumps(contenido, indent=4)
        archivo.write(guardar)


#FUNCIONES PARA CONSULTAR

def mini_verification(mensaje = "Presione ENTER para continuar ..."):
    input(f"\n{mensaje}")

def consultar_cliente():
    usuarios = leer_json(archivo_usuarios)
    

    opc = 0
    while True:
        opc = int(input("""
                        
        Presione "1" para consultar el cliente
        Presione "2" para volver: """))

        if opc == 1:
            usuario_id = input("Ingrese el ID del cliente que desea consultar: ")
            for nombre, datos in usuarios.items():
                if datos.get("id") == usuario_id:
                    print(f"Datos del cliente: {nombre} - {datos}")
                    return
            print("Revise el ID ingresado, dato no encontrado")

        elif opc == 2:
            break
    mini_verification("Presione ENTER para volver al MENÚ DE CLIENTES ...")


def consultar_instructores():
    instructores = leer_json(archivo_instructores)

    opc = 0
    while True:
        opc = int(input("""Presione "1" para consultar el instructor o "2" para volver: """))

        if opc == 1:
            usuario_id = input("Ingrese el ID del instructor que desea consultar: ")
            for nombre, datos in instructores.items():
                if datos.get("id") == usuario_id:
                    print(f"Datos del instructor: {nombre} - {datos}")
                    return
            print("Revise el ID ingresado, dato no encontrado")

        elif opc == 2:
            break
    mini_verification()

def consultar_vehiculo():
    vehiculos = leer_json(archivo_vehiculos)

    opc = 0
    while True:
        opc = int(input("""Presione "1" para consultar el vehículo o "2" para volver: """))

        if opc == 1:
            placa_id = input("Ingrese la placa del vehículo: ")

            for placa, datos in vehiculos.items():
                if placa == placa_id:
                    print(f"Datos del vehículo: {placa} - {datos}")
                    return

            print("Revise la placa ingresada, dato no encontrado")

        elif opc == 2:
            break
    mini_verification()


def buscar_cita():

    palabra = input("Ingrese la fecha o el nombre que desea filtrar")

    datos = leer_json(archivo_citas)

    for info in datos:
        if palabra in datos[info]["cliente"] or palabra in datos[info]["fecha"]:
            print(datos[info])
        else:
            print("Ingrese una opción válida")


#FUNCIONES PARA REGISTRAR



def input_cliente():
    nombre = input("Ingrese el nombre del nuevo cliente: ").strip().title()
    id_cliente = input("Ingrese el ID del nuevo cliente: ")

    datos = leer_json(archivo_usuarios)

    for clave, valor in datos.items():
        if valor["id"] == id_cliente:
            print("El usuario con ese ID ya existe")
            return

    telefono = input("Ingrese el numero de celular del cliente: ")

    datos[nombre] = {
        "id": id_cliente,
        "telefono": telefono
    }

    escribir_json(archivo_usuarios, datos)

    print("El cliente ingresado ha sido guardado exitosamente")

    mini_verification()


def input_vehiculos():
    placa_id = input("Ingrese la placa del vehículo: ").strip().upper()
    
    datos = leer_json(archivo_vehiculos)

    if placa_id in datos:
        print("El vehículo con esa placa ya existe")
        return

    tipo = input("Ingrese si es moto o auto: ").strip().lower()

    datos[placa_id] = {
        "tipo": tipo,
        "disponible": True
    }

    escribir_json(archivo_vehiculos, datos)

    print("El vehículo ha sido guardado exitosamente")

    mini_verification()



def input_instructores():
    nombre = input("Ingrese el nombre del instructor: ").strip().title()
    id_instructor = input("Ingrese el ID del instructor: ").strip()

    datos = leer_json(archivo_instructores)

    for clave, valor in datos.items():
        if valor["id"] == id_instructor:
            print("El instructor con ese ID ya existe")
            return

    especialidad = input("Ingrese si es instructor para carro o moto: ").strip().lower()

    datos[nombre] = {
        "id": id_instructor,
        "especialidad": especialidad,
        "disponible": True
    }

    escribir_json(archivo_instructores, datos)

    print("El instructor ingresado ha sido guardado exitosamente")

    mini_verification()




def buscar_historial_cliente():

    datos = leer_json(archivo_citas)

    opc = 0
    while True:
        opc = int(input(""" 
        Presione "1" para consultar.
        Presione "2" para volver: """))

        if opc == 1:
            palabra = input("Ingrese el id del cliente")

            for info in datos:
                if palabra == datos[info]["cliente_id"]:
                    print(datos[info], "\n")

            print("Revise el id ingresado, dato no encontrado")

        elif opc == 2:
            break

    mini_verification()

def mostrar_todos_clientes():

    datos = leer_json(archivo_usuarios)
    opc = 0

    while True:
        opc = int(input(""" 
        Presione "1" para consultar.
        Presione "2" para volver: """))

        if opc == 1:
            for info in datos:
                print(info)
                print(datos[info], "\n")
        elif opc == 2:
            break
        else:
            print("Ingrese una opción válida")
    mini_verification()


def mostrar_historial_completo():

    datos = leer_json(archivo_citas)
    opc = 0

    while True:
        opc = int(input(""" 
        Presione "1" para consultar.
        Presione "2" para volver: """))

        if opc == 1:
            for info in datos:
                print(datos[info], "\n")
        elif opc == 2:
            break
        else:
            print("Ingrese una opción válida")
    mini_verification()
        

