from json import load, dumps

def leer_json(archivito):
    respuesta = {}
    with open(archivito, "r") as archivo:
        respuesta = load(archivo)
        return respuesta
    
def escribir_json(archivito, devuelve):
    with open(archivito, "w") as archivo:
        guardar = dumps(devuelve, ident=4)
        archivo.write(guardar)
