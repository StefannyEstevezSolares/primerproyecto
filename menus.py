def menu_princial():
    print("""
==============BIENVENIDO AL MENÚ PRINCIPAL=================
          
          INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR
          1. Gestión de clientes
          2. Gestión de instructores
          3. Gestión de vehículos
          4. Gestión de citas
          5. PARA SALIR
          
""")

def menu_clientes():
    print("""

=======================MENÚ DE CLIENTES=======================
          
          1. Registrar cliente
          2. Consultar cliente
          3. Historial de cliente
          4. Volver al menú principal 


          """)
    

def menu_instructores():
    print("""

=======================MENÚ DE INSTRUCTORES=======================
          
          1. Registrar instructores
          2. Consultar instructores
          3. Volver al menú principal 

          """)
    

def menu_vehiculos():
    print("""

=======================MENÚ DE VEHÍCULOS=======================
          
          1. Registrar vehículos
          2. Consultar vehículos
          3. Volver al menú principal 

          """)
    


def menu_citas():
    print("""

=======================MENÚ DE CITAS=======================
          
          1. Programar citas
          2. Consultar historial de citas por cliente
          3. Consultar historial entero
          4. Consultar historial de clientes que asistieron
          5. Consultar historial de clientes que no asistieron
          6. Modificar asistencia
          7. Agregar observaciones
          8. Volver al menú principal 

          """)
    

def separador():
    print("="*50)

def opcion():
    opc= int(input("Ingrese su opción "))
    return opc