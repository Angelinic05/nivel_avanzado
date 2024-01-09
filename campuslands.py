import campers
import entrenadores

def menu_principal():
    while True:
        print("1. Registrar Camper\n2. Asignar Ruta a Camper\n3. Evaluar Camper\n4. Campers en Riesgo\n5. Registrar Entrenador\n6. Asignar Ruta a Entrenador\n7. Obtener Entrenadores\n8. Reportes\n9. Salir")
        opcion = input(":)").lower()

        if opcion == '1':
            campers.registrar_camper()
        elif opcion == '2':
            camper_id = input("Ingrese el ID del Camper: ")
            ruta = input("Ingrese la Ruta a asignar: ")
            campers.asignar_ruta(camper_id, ruta)
        elif opcion == '3':
            camper_id = input("Ingrese el ID del Camper: ")
            nota_teorica = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))
            campers.evaluar_camper(camper_id, nota_teorica, nota_practica)
        elif opcion == '4':
            campers.campers_en_riesgo()
        elif opcion == '5':
            entrenadores.registrar_entrenador()
        elif opcion == '6':
            entrenador_id = input("Ingrese el ID del Entrenador: ")
            ruta = input("Ingrese la Ruta a asignar: ")
            entrenadores.asignar_ruta_entrenador(entrenador_id, ruta)
        elif opcion == '7':
            entrenadores.obtener_entrenadores_trabajando()
        elif opcion == '8':
            menu_reportes()
        elif opcion == '9':
            break

def menu_reportes():
    while True:
        print("a. Listar campers en estado de inscrito\nb. Listar campers que aprobaron el examen inicial\nc. Listar entrenadores trabajando\nd. Listar campers con bajo rendimiento\ne. Listar campers y entrenador asociados a una ruta de entrenamiento\nf. Mostrar estadísticas de aprobación y reprobación por módulo\ng. Regresar al menú principal")
        opcion_reporte = input(":)").lower()

        if opcion_reporte == 'a':
            campers.listar_campers_estado("inscrito")
        elif opcion_reporte == 'b':
            campers.listar_campers_aprobados()
        elif opcion_reporte == 'c':
            entrenadores.obtener_entrenadores_trabajando()
        elif opcion_reporte == 'd':
            campers.listar_campers_bajo_rendimiento()
        elif opcion_reporte == 'e':
            # Agregar lógica para listar campers y entrenador asociados a una ruta de entrenamiento
            pass
        elif opcion_reporte == 'f':
            # Agregar lógica para mostrar estadísticas de aprobación y reprobación por módulo
            pass
        elif opcion_reporte == 'g':
            break

if __name__ == "__main__":
    menu_principal()
