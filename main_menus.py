from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import leer_json, escribir_json, consultar_auto, consultar, consultar_cita


def menu_principal():
    while True: 
        principal()
        opc = opcion()
        if opc == 1:
            if iniciar_sesion() != False:
                menu_clientes()
        elif opc == 2:
            if iniciar_sesion == "instructor":
                menu_instructores()
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
            consultar()
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
            consultar_auto
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
            consultar_cita()
        elif opc == 3: 
            print("Historial de citas(todas)") 
            break
        else:
            print("Valor invalido")

#GESTION DE USUARIOS

archivo_usuarios = "usuarios.json"


def iniciar_sesion():
    nombre = input("Ingrese su usuario")
    clave = input("Ingrese su contraseña")
    usuarios = leer_json(archivo_usuarios)
    usuario = usuarios.get(nombre, None)
    if usuario != None:
        if usuario["contrasena"] == clave:
            input("ENTER PARA CONTINUAR")
            return usuario["tipo"]
        else:
            print("Contraseña Incorrecta")
            input("ENTER PARA CONTINUAR")
            return False


menu_principal()