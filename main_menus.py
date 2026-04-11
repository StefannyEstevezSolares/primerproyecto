from menus import menu_instructores as instructores, menu_citas as citas, menu_clientes as clientes, menu_instructores as instructores, menu_princial as principal, menu_vehiculos as vehiculos, opcion
from funcionalidades import consultar_vehiculo,  consultar_instructores, consultar_cliente , buscar_historial_cliente, mini_verification
from funcionalidades import input_cliente, input_instructores, input_vehiculos, mostrar_historial_completo , buscar_historial_cliente , mostrar_todos_clientes
from funcionalidades_citas import buscar_cliente_nombre_fecha, mostrar_asistencias, manipular_asistencia, escribir_comentario, pedir_fecha, pedir_hora, input_cita


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
            input_vehiculos()
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
            input_cita()
        elif opc == 2:
            buscar_cliente_nombre_fecha()
        elif opc == 3:
            buscar_historial_cliente()
        elif opc == 4:
            mostrar_historial_completo()
        elif opc == 5: 
            mostrar_asistencias(True)
        elif opc == 6:
            mostrar_asistencias(False)
        elif opc == 7:
            manipular_asistencia()
        elif opc == 8:
            escribir_comentario()
        elif opc == 9:
            print("Volver al menú anterior")
            break
        else:
            print("Valor invalido")

