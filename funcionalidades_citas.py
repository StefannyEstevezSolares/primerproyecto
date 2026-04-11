from json import dumps, load
from datetime import datetime

#DICCIONARIOS PARA LOS ARCHIVOS JSON

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



#FUNCIONES DE VALIDACIÓN DE HORA Y FECHA 


def pedir_fecha():
    while True:
        fecha_usuario = input("Ingrese la fecha (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(fecha_usuario, "%Y-%m-%d")
            return fecha_usuario
        except:
            print("Formato incorrecto, intente nuevamente")


def pedir_hora():
    while True:
        hora_usuario = input("Ingrese la hora (HH:MM): ").strip()

        try:
            datetime.strptime(hora_usuario, "%H:%M")
            return hora_usuario
        except:
            print("Hora inválida, intente nuevamente")


#VALIDACIÓN DE HISTORIAL Y CITAS


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



def buscar_cliente_nombre_fecha():
    citas = leer_json(archivo_citas)

    opc = input("¿Desea buscar por (1) fecha o (2) nombre del cliente? ")

    if opc == "1":
        fecha_buscar = pedir_fecha()
        encontrado = False

        for id_cita, datos in citas.items():
            if datos["fecha"] == fecha_buscar:
                print(datos, "\n")  
                encontrado = True

        if not encontrado:
            print("No se encontraron citas para esa fecha.")

    elif opc == "2":
        nombre_buscar = input("Ingrese el nombre del cliente: ").strip()
        encontrado = False

        for id_cita, datos in citas.items():
            if datos["cliente_nombre"].strip().title() == nombre_buscar.title():
                print(datos, "\n")
                encontrado = True

        if not encontrado:
            print("No se encontraron citas para ese cliente.")

    else:
        print("Opción inválida. Debe elegir 1 o 2.")


def input_cita():

    vehiculos = leer_json(archivo_vehiculos)
    instructores = leer_json(archivo_instructores)
    clientes = leer_json(archivo_usuarios)
    citas = leer_json(archivo_citas)

    id_cliente = input("Ingrese el ID del cliente: ")

    for clave, valor in clientes.items():
        if valor["id"] == id_cliente:
            break
    else:
        print("El cliente debe ser agregado primero en la sección de clientes")
        return

    nombre_cliente = input("Ingrese el nombre y apellido del cliente: ")

    fecha = pedir_fecha()
    hora = pedir_hora()

    instructor_id = input("Ingrese el id del instructor que ingresará a la cita: ")

    instructor_aprobado = None
    instructorKey = None
    for cl, valor in instructores.items():
        if valor['id'] == instructor_id:
            instructorKey = cl
            instructor_aprobado = valor
            break

    if not instructor_aprobado:
        print("El instructor no existe en el sistema")
        return

    if instructor_aprobado['disponible'] != True:
        print("El instructor no está disponible")
        return

    for clave, valor in citas.items():
        fecha_apartada = valor["fecha"]
        hora_apartada = valor["hora"]
        estado = valor["estado_de_cita"]
        instructor_cita = valor["instructor_asigado"]

        if fecha_apartada == fecha and hora_apartada == hora and estado == "apartado" and instructor_cita == instructor_id:
            print("El instructor ya tiene una cita apartada para esa fecha y hora, por favor elija otro horario o instructor")
            return

    while True:
        print("\n")
        opc = int(input("Ingrese 1 para apartar una moto.\nIngrese 2 para apartar un carro.\n"))

        vehiculo_seleccionado = None

        if opc == 1:
            for clave, valor in vehiculos.items():
                if valor["tipo"] == "moto" and valor["disponible"] == True:
                    vehiculo_seleccionado = clave
                    break
            else:
                print("No hay motos disponibles")
                return

        elif opc == 2:
            for clave, valor in vehiculos.items():
                if valor["tipo"] == "carro" and valor["disponible"] == True:
                    vehiculo_seleccionado = clave
                    break
            else:
                print("No hay autos disponibles")
                return

        if vehiculo_seleccionado:
            break

    duracion = input("Ingrese la duración de la cita (1h): ")

    nueva_cita = {
        "cliente_id": id_cliente,
        "cliente_nombre": nombre_cliente,
        "instructor_asigado": instructor_id,
        "tipo_vehiculo": vehiculos[vehiculo_seleccionado]["tipo"],
        "fecha": fecha,
        "hora": hora,
        "asistencia": False,
        "comentario": "",
        "duracion": duracion,
        "estado_de_cita": "apartado"
    }

    if citas:
        id_cita = str(int(max(citas.keys())) + 1)
    else:
        id_cita = "001"

    citas[id_cita] = nueva_cita

    escribir_json(archivo_citas, citas)

    vehiculos[vehiculo_seleccionado]["disponible"] = False
    instructores[instructorKey]
    instructores[instructorKey]["disponible"] = False

    escribir_json(archivo_vehiculos, vehiculos)
    escribir_json(archivo_instructores, instructores)

    print("La cita ha sido programada exitosamente")
    return True


