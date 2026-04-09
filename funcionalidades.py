from json import load, dumps

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

def consultar(usuario):
    usuarios = leer_json(archivo_usuarios)
    datos = usuarios.get(usuario)
    if datos:
        print(f"Nombre de usuario :{datos}")
    else:
        print("Dato no encontrado")

def consultar_instructores(usuario):
    usuarios = leer_json(archivo_instructores)
    datos = usuarios.get(usuario)
    if datos:
        print(f"Datos del vehículo:{datos}")
    else:
        print("Dato no encontrado")

def consultar_auto(placa):
    auto = leer_json(archivo_vehiculos)
    datos = auto.get(placa)
    if datos:
        print(f"Datos del vehículo:{datos}")
    else:
        print("Dato no encontrado")


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

    palabra = input("Ingrese el id o el nombre del cliente")

    datos = leer_json(archivo_citas)

    for info in datos:
        if palabra in datos[info]["id"]:
            print(datos[info])
        else:
            print("Ingrese una opción válida")


def buscar_historial():

    datos = leer_json(archivo_citas)
    for info in datos:
        print(datos[info])
        


#Validación de citas


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


