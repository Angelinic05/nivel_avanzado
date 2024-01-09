entrenadores_db = {}

def registrar_entrenador():
    entrenador_id = input("Ingrese el ID del Entrenador: ")
    nombre = input("Ingrese el nombre del Entrenador: ")
    
    entrenador = {
        "nombre": nombre,
        "rutas_asignadas": []
    }

    entrenadores_db[entrenador_id] = entrenador
    print(f"Entrenador {nombre} registrado con éxito.")

def asignar_ruta_entrenador(entrenador_id, ruta):
    if entrenador_id in entrenadores_db:
        if ruta not in entrenadores_db[entrenador_id]["rutas_asignadas"]:
            entrenadores_db[entrenador_id]["rutas_asignadas"].append(ruta)
            print(f"Ruta {ruta} asignada al Entrenador {entrenadores_db[entrenador_id]['nombre']}.")
        else:
            print(f"El Entrenador {entrenadores_db[entrenador_id]['nombre']} ya tiene asignada la Ruta {ruta}.")
    else:
        print(f"No se encontró el Entrenador con ID {entrenador_id}.")

def obtener_entrenadores_trabajando():
    print("Entrenadores trabajando con Campuslands:")
    for entrenador_id, entrenador in entrenadores_db.items():
        if entrenador["rutas_asignadas"]:
            print(f"{entrenador_id}: {entrenador['nombre']} - Rutas: {', '.join(entrenador['rutas_asignadas'])}")

# Agrega más funciones según sea necesario
