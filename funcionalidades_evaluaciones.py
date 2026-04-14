from json import dumps, load
from datetime import datetime


def mini_verification(mensaje = "Presione ENTER para continuar ..."):
    input(f"\n{mensaje}")

#DICCIONARIOS PARA LOS ARCHIVOS JSON

archivo_usuarios = "data/usuarios.json"
archivo_vehiculos = "data/vehiculos.json"
archivo_citas = "data/citas.json"
archivo_instructores = "data/instructores.json"
archivo_evaluaciones = "data/evaluaciones.json"


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


def input_evaluacion():

    id_evaluacion = input("Ingrese el ID de la evaluación: ").strip()
    evaluaciones = leer_json(archivo_evaluaciones)
    instructores = leer_json(archivo_instructores)

    nombre = input("Ingrese el nombre del nuevo estudiante: ").strip().title()
    id_estudiante = input("Ingrese el ID del nuevo estudiante: ")

    if nombre == "" or id_estudiante == "":
        print("El campo nombre o ID no pueden estar vacíos")
        return

    fecha = pedir_fecha()

    instructor_id = input("Ingrese el id del instructor que ingresará a la evaluación: ")

    instructor_aprobado = None
    instructorKey = None
    for cl, valor in instructores.items():
        if valor['id'] == instructor_id:
            instructorKey = cl
            instructor_aprobado = cl
            break

    if not instructor_aprobado:
        print("El instructor no existe en el sistema")
        return

    try:
        nota = float(input("Ingrese la calificación del estudiante: "))
        if nota > 100 or nota < 0:
            print("La calificación debe estar entre 0 y 100")
            return
    except:
        print("La calificación debe ser un número entero")
        return
    
    

    evaluaciones[id_evaluacion] = {
        "id_estudiante": id_estudiante,
        "nombre_estudiante": nombre,
        "instructor_asigado": instructor_aprobado,
        "fecha": fecha,
        "calificacion": nota
    }

    
    


    

    escribir_json(archivo_evaluaciones, evaluaciones)

    print("La evaluación ha sido programada exitosamente")
    mini_verification()
    return True



def consultar_evaluaciones():
    evaluaciones = leer_json(archivo_evaluaciones)

    opc = 0
    while True:
        try:
            opc = int(input("""Presione "1" para consultar el estudiante o "2" para volver: """))

            if opc == 1:
                evaluacion_id = input("Ingrese el ID del estudiante que desea consultar: ")
                for nombre, datos in evaluaciones.items():
                    if datos.get("id_estudiante") == evaluacion_id:
                        print(f"Datos del estudiante: {nombre} - {datos}")
                        return
                print("Revise el ID ingresado, dato no encontrado")

            elif opc == 2:
                break
        except:
            print("Ingrese una opción válida")

def calcular_promedio_general():
    evaluaciones = leer_json(archivo_evaluaciones)
    
    if not evaluaciones:
        print("No hay evaluaciones registradas para calcular el promedio.")
        return

    total_calificaciones = 0
    cantidad_evaluaciones = 0

    opc = 0

    while True:
        try:
            opc = int(input("""Presione "1" para calcular el promedio o "2" para volver: """))
            if opc == 1:

                for evaluacion in evaluaciones.values():
                    calificacion = evaluacion.get("calificacion")
                    if isinstance(calificacion, (int, float)):
                        total_calificaciones += calificacion
                        cantidad_evaluaciones += 1

                if cantidad_evaluaciones == 0:
                    print("No hay calificaciones válidas para calcular el promedio.")
                    return

                promedio = total_calificaciones / cantidad_evaluaciones
                print(f"El promedio general de las evaluaciones es: {promedio:.2f} total de evaluaciones: {cantidad_evaluaciones}")
                mini_verification() 
                return promedio
            if opc == 2:
                break
        except:
            print("Ingrese una opción válida")



