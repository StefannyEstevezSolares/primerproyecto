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
    nombre = input("Ingrese el nombre del cliente")
    id = input("Ingrese el id del cliente")

    cliente = {
        "nombre" : nombre,
        "id" : id 
    }
    
    datos = leer_json(archivo_usuarios)
    datos[nombre] = cliente

    escribir_json(archivo_usuarios, datos)

    print("Cliente registrado con éxito")
    mini_verification("Ingrese ENTER para volver al MENÚ DE CLIENTES ...")

def input_vehiculo():
    placa = input("Ingrese la placa del vehiculo")
    tipo = input("¿Qué tipo de vehículo es este?")
   

    vehiculo = {
        "placa" : placa,
        "tipo" : tipo,

    }
    
    datos = leer_json(archivo_usuarios)
    datos[placa] = vehiculo

    escribir_json(archivo_vehiculos, datos)
    mini_verification("Ingrese ENTER para volver al MENÚ DE VEHICULOS ...")


def input_instructores():
    nombre = input("Ingrese el nombre del nuevo instructor")
    contrasena = input("Ingrese la contrasea del nuevo instructor")
    tipo = input("¿Qué tipo de usuario es este?")
    especialidad = input("¿Cuál es la especialidad de este instructor")
    

    nuevo_usuario = {
        "nombre" : nombre,
        "contrasena" : contrasena,
        "tipo" : tipo,
        "especialidad" : especialidad,

    }
    
    datos = leer_json(archivo_instructores)
    datos[nombre] = nuevo_usuario




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
        

#VALIDACIÓN DE HISTORIAL Y CITAS

def input_citas():

    instructor_asignado = input("Ingrese el instructor asignado: ").strip().title()
    id_cita = input("Ingrese el nuevo id de la cita: ").strip()
    cliente = input("Ingrese nombre del cliente: ").strip().title()
    tipo_auto = input("¿Cuál es el tipo de auto? ").strip().lower()
    fecha = input("¿Cuál es la fecha de la cita? ")
    hora = input("Ingrese la hora (24h, ej: 18:00): ")
    duracion = input("Ingrese la duración (1 o 2 horas): ")

    
    instructores = leer_json("instructores.json")
    vehiculos = leer_json("vehiculos.json")
    citas = leer_json("citas.json")


    if instructor_asignado not in instructores:
        print("El instructor no existe")
        return

    instructor = instructores[instructor_asignado]

    if not instructor["disponible"]:
        print("El instructor no está disponible")
        return

    if instructor["especialidad"] != tipo_auto:
        print("El instructor no tiene esa especialidad")
        return

    vehiculo_encontrado = None

    for placa, datos in vehiculos.items():
        if datos["tipo"] == tipo_auto and datos["disponible"]:
            vehiculo_encontrado = placa
            break

    if vehiculo_encontrado is None:
        print("No hay vehículos disponibles para ese tipo")
        return

    nueva_cita = {
        "id": id_cita,
        "cliente": cliente,
        "instructor": instructor_asignado,
        "vehiculo": vehiculo_encontrado,
        "tipo_auto": tipo_auto,
        "fecha": fecha,
        "hora": hora,
        "duracion": duracion
    }

    citas[id_cita] = nueva_cita
    escribir_json("citas.json", citas)

    instructores[instructor_asignado]["disponible"] = False
    vehiculos[vehiculo_encontrado]["disponible"] = False

    escribir_json("instructores.json", instructores)
    escribir_json("vehiculos.json", vehiculos)

    print("Cita registrada con éxito")

def escribir_comentario():
    
    citas= leer_json("citas.json")

    id_citas = input("Ingrese el ID de la cita para buscar la cita que desea comentar")

    if id_citas in citas:
        print(citas[id_citas])

    else:
        print("Registro inválido")
        
    opc = 0

    while True:
    
        opc = int(input("""¿Desea agregar un comentario?
                    
                    1. Si
                    2. Volver
              """))
        
        
        
        if opc == 1: 
            comentar= input("Escriba su comentario")
            citas[id_citas]["comentario"] = comentar

            escribir_json("citas.json" , citas)
        
            print("Comentario Ingresado Correctamente")
            break

        elif opc == 2:
            break


def manipular_asistencia():

    citas = leer_json("citas.json")
    id_citas = input("Ingrese el ID de la cita a modificar")
        
    if id_citas in citas:
        print(citas[id_citas])
    else:
        print("Registro inválido")

    opc = 0
    while True:
        opc = int(input("""Presione las siguientes opciones para modificar la asistencia:
               
                    1. Usuario si asistió
                    2. Usuario no asisitió
                    3. Volver
                    
                    "Ingrese    """))
        
        if opc == 1:
            
            citas[id_citas]["asistencia"] = True
            escribir_json("citas.json", citas)
            print(f" La asistencia para cita {id_citas} se modificó con éxito")

        elif opc == 2:
            citas[id_citas]["asistencia"] = False
            escribir_json("citas.json", citas)
            print(f" La asistencia para cita {id_citas} se modificó con éxito")


        elif opc == 3:
            break

def mostrar_asistencias(value):
    
    citas = leer_json("citas.json")
    for id_citas, datos in citas.items():
        if datos ["asistencia"] == value:
            print(datos)
            







