campers_db = {}

def registrar_camper():
    camper_id = input("Ingrese el ID del Camper: ")
    nombre = input("Ingrese el nombre del Camper: ")
    apellidos = input("Ingrese los apellidos del Camper: ")
    direccion = input("Ingrese la dirección del Camper: ")
    acudiente = input("Ingrese el nombre del acudiente del Camper: ")
    celular = input("Ingrese el número de celular del Camper: ")
    fijo = input("Ingrese el número fijo del Camper: ")
    estado = "inscrito"
    
    camper = {
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "celular": celular,
        "fijo": fijo,
        "estado": estado,
        "ruta_asignada": None,
        "nota_final": None
    }

    campers_db[camper_id] = camper
    print(f"Camper {nombre} {apellidos} registrado con éxito.")

def asignar_ruta(camper_id, ruta):
    if camper_id in campers_db:
        campers_db[camper_id]["ruta_asignada"] = ruta
        print(f"Ruta {ruta} asignada al Camper {campers_db[camper_id]['nombre']} {campers_db[camper_id]['apellidos']}.")
    else:
        print(f"No se encontró el Camper con ID {camper_id}.")

def evaluar_camper(camper_id, nota_teorica, nota_practica):
    if camper_id in campers_db:
        promedio = (nota_teorica * 0.3) + (nota_practica * 0.6)
        campers_db[camper_id]["nota_final"] = promedio
        estado = "aprobado" if promedio >= 60 else "reprobado"
        campers_db[camper_id]["estado"] = estado
        print(f"Camper {campers_db[camper_id]['nombre']} {campers_db[camper_id]['apellidos']} evaluado con éxito. Estado: {estado}")
    else:
        print(f"No se encontró el Camper con ID {camper_id}.")

def campers_en_riesgo():
    print("Campers en riesgo:")
    for camper_id, camper in campers_db.items():
        if camper["estado"] == "inscrito" and camper.get("nota_final", 0) < 60:
            print(f"{camper_id}: {camper['nombre']} {camper['apellidos']}")

def listar_campers_aprobados():
    print("Campers que aprobaron el examen inicial:")
    for camper_id, camper in campers_db.items():
        if camper["estado"] == "aprobado":
            print(f"{camper_id}: {camper['nombre']} {camper['apellidos']}")

def listar_campers_bajo_rendimiento():
    print("Campers con bajo rendimiento:")
    for camper_id, camper in campers_db.items():
        if camper["estado"] == "inscrito" and camper.get("nota_final", 0) < 60:
            print(f"{camper_id}: {camper['nombre']} {camper['apellidos']}")
