import json


def guardar_data(objetos, arch: str):
    objetos_serializados = []
    for obj in objetos:
        if hasattr(obj, '__dict__'):
            objetos_serializados.append(obj.__dict__)
        else:
            print("Hubo un error")
    
    with open(arch,"w") as file:
        json.dump(objetos_serializados,file,indent=4)
    return objetos_serializados

