from json import load, dumps

archivo_usuarios = "usuarios.json"
archivo_vehiculos = "vehiculos.json"
archivo_citas = "citas.json"
archivo_instructores = "instructores.json"

def leer_json(archivito):
    respuesta = {}
    with open(archivito, "r") as archivo:
        respuesta = load(archivo)
        return respuesta
    
def escribir_json(archivito, contenido):
    with open(archivito, "w") as archivo:
        guardar = dumps(contenido, indent=4)
        archivo.write(guardar)

def consultar(usuario):
    usuarios = leer_json(archivo_usuarios)
    datos = usuarios.get(usuario)
    if datos:
        print(f"Nombre de usuario : {usuario}, {datos}")
    else:
        print("Dato no encontrado")


def consultar_auto(placa):
    auto = leer_json(archivo_vehiculos)
    datos = auto.get(placa)
    if datos:
        print(f"Datos del vehículo:{datos}")
    else:
        print("Dato no encontrado")


def consultar_cita(id_cita):
    cita = leer_json(archivo_citas)
    datos = cita.get(id_cita)
    if datos:
        print(f"Datos de la cita: {datos}")
    else:
        print("Dato no encontrado")

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
    disponible = input("¿Está disponible?")

    vehiculo = {
        "placa" : placa,
        "tipo" : tipo,
        "disponible" : disponible

    }
    
    datos = leer_json(archivo_usuarios)
    datos[placa] = vehiculo

    escribir_json(archivo_vehiculos, datos)

def input_instructores():
    nombre = input("Ingrese el nombre del nuevo instructor")
    contrasena = input("Ingrese la contrasea del nuevo instructor")
    tipo = input("¿Qué tipo de usuario es este?")
    especialidad = input("¿Cuál es la especialidad de este instructor")
    disponible = input("¿El instructor está disponible?")

    nuevo_usuario = {
        "nombre" : nombre,
        "contrasena" : contrasena,
        "tipo" : tipo,
        "especialidad" : especialidad,
        "disponible" : disponible

    }
    
    datos = leer_json(archivo_instructores)
    datos[nombre] = nuevo_usuario

def input_citas():
    id = input("Ingrese el nuevo id de la cita")
    cliente = input("Ingrese nombre del cliente")
    instructor_asignado = input("Ingrese el instructor asignado")
    tipo_auto = input("¿Cuál es el tipo de auto")
    fecha = input("¿Cuál es la fecha de la cita?")
    hora = input("Ingrese la hora de la cita en un formato de 24 horas(ejemplo: 18:00))")
    duracion = input("Ingrese la duración de la cita 1 o 2 horas")
    #observaciones = input("Ingrese observaciones que pueda tener acerca de la cita")

    nuevo_usuario = {
        "id" : id,
        "instructor_asignado" : instructor_asignado,
        "tipo_auto" : tipo_auto,
        "fecha" : fecha,
        "hora" : hora,
        "duracion" : duracion

    }
    
    datos = leer_json(archivo_instructores)
    datos[nombre] = nuevo_usuario

    escribir_json(archivo_vehiculos, datos)


