from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import leer_json, escribir_json, consultar_auto, consultar, consultar_cita, consultar_instructores
from funcionalidades import input_citas, input_cliente, input_instructores, input_vehiculo

def menu_principal():
    while True: 
        principal()
        opc = opcion()
        if opc == 1:
            menu_clientes()
        elif opc == 2:
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
            input_cliente()
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
            input_instructores()
        elif opc == 2:
            consultar_instructores()
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
            input_vehiculo()
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
            input_citas()
        elif opc == 2:
            consultar_cita()
        elif opc == 3: 
            print("Historial de citas(todas)") 
            break
        else:
            print("Valor invalido")

#GESTION DE USUARIOS

archivo_usuarios = "usuarios.json"


menu_principal()