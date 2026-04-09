from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import leer_json, escribir_json, consultar_auto, consultar, consultar_instructores
from funcionalidades import input_citas, input_cliente, input_instructores, input_vehiculo , buscar_cita , buscar_historial , buscar_historial_cliente

def menu_principal():
    while True: 
        principal()
        opc = opcion()
        if opc == 1:
            menu_clientes()
        elif opc == 2:
            menu_instructores()
        elif opc == 3: 
            menu_vehiculos
        elif opc == 4:
            menu_citas()
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
            buscar_historial_cliente()
        elif opc == 4: 
            menu_principal
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
            menu_principal()
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
            consultar_auto()
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
            buscar_historial_cliente()
        elif opc == 3:
            buscar_historial()
        elif opc == 3: 
            print("Historial de citas(todas)") 
            break
        else:
            print("Valor invalido")

#GESTION DE USUARIOS

archivo_usuarios = "usuarios.json"


menu_principal()