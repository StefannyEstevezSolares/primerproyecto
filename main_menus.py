from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import consultar_vehiculo,  consultar_instructores, consultar_cliente , buscar_historial_cliente, 
from funcionalidades import input_citas, input_cliente, input_instructores, input_vehiculo , mostrar_historial_completo , buscar_historial_cliente , mostrar_todos_clientes

def menu_principal():
    while True: 
        principal()
        opc = opcion()
        if opc == 1:
            menu_clientes()
        elif opc == 2:
            menu_instructores()
        elif opc == 3: 
            menu_vehiculos()
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
            consultar_cliente()
        elif opc == 3:
            mostrar_todos_clientes()
        elif opc == 4: 
            buscar_historial_cliente()
        elif opc == 5: 
            menu_principal()
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
            consultar_vehiculo()
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

menu_principal()