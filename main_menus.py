from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import leer_json, escribir_json
def menu_principal():
    while True: 
        principal()
        opc = opcion()
        if opc == 1:
            print("GESTION DE CLIENTES")
        elif opc == 2:
            print("GESTIÓN DE INSTRUCTORES")
        elif opc == 3: 
            print("GESTIÓN DE VEHICULOS")
        elif opc == 4:
            print("GESTION DE CITAS")
        elif opc == 5: 
            print("SALIR") 
            break
        else:
            print("Valor invalido")


def menu_clientes():
    while True: 
        clientes()
        opc = opcion()
        if opc == 1:
            print("Registrar Cliente")
        elif opc == 2:
            print("Consultar Cliente")
        elif opc == 3: 
            print("Historial Cliente")
        elif opc == 4: 
            print("Volver al menú anterior") 
            break
        else:
            print("Valor invalido")

#GESTION DE INSTRUCTORES


def menu_instructores():
    while True: 
        instructores()
        opc = opcion()
        if opc == 1:
            print("Registrar Instructor")
        elif opc == 2:
            print("Consultar Instructor")
        elif opc == 3: 
            print("Volver al menú anterior") 
            break
        else:
            print("Valor invalido")

def menu_vehiculos():
    while True: 
        vehiculos()
        opc = opcion()
        if opc == 1:
            print("Registrar Vehiculo")
        elif opc == 2:
            print("Consultar Vehículo")
        elif opc == 3: 
            print("Volver al menú anterior") 
            break
        else:
            print("Valor invalido")


def menu_citas():
    while True: 
        citas()
        opc = opcion()
        if opc == 1:
            print("Programar cita")
        elif opc == 2:
            print("Consultar citas")
        elif opc == 3: 
            print("Historial de citas(todas)") 
            break
        else:
            print("Valor invalido")

#GESTION DE USUARIOS

archivo_usuarios = "usuarios.json"


def iniciar_sesion_cliente():
    nombre = ("Ingrese su usuario")
    password = ("Ingrese su contraseña")
    usuarios = leer_json(archivo_usuarios)
    user = usuarios.get(nombre, None)
    if user != None:
        

    else:
        print("usuario no existe")
        return False

