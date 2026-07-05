from database import cliente
from funciones_trabajadores import eliminar_trabajador, registrar_trabajador, listar_trabajadores, actualizar_trabajador
from funciones_proyectos import crear_proyecto, eliminar_trabajador_de_proyecto, listar_proyectos, asignar_trabajador_a_proyecto
from funciones_tareas import crear_tarea, listar_tareas_por_proyecto, actualizar_estado_tarea
from funciones_reportes import ver_avance_proyecto, reporte_por_trabajador

def mostrar_menu():
    print("\n" + "="*50)
    print("        DEVELOW MANAGER - GESTION DE PROYECTOS")
    print("="*50)
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Actualizar trabajador")
    print("4. Crear proyecto")
    print("5. Listar proyectos")
    print("6. Asignar trabajador a proyecto")
    print("7. Crear tarea")
    print("8. Listar tareas por proyecto")
    print("9. Actualizar estado de tarea")
    print("10. Ver avance de proyecto")
    print("11. Generar reporte por trabajador")
    print("12. Eliminar trabajador")
    print("13. eliminar trabajador de proyecto")
    print("16. Salir")
    print("="*50)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            actualizar_trabajador()
        elif opcion == "4":
            crear_proyecto()
        elif opcion == "5":
            listar_proyectos()
        elif opcion == "6":
            asignar_trabajador_a_proyecto()
        elif opcion == "7":
            crear_tarea()
        elif opcion == "8":
            listar_tareas_por_proyecto()
        elif opcion == "9":
            actualizar_estado_tarea()
        elif opcion == "10":
            ver_avance_proyecto()
        elif opcion == "11":
            reporte_por_trabajador()
        elif opcion == "12":
            eliminar_trabajador()
        elif opcion == "13":
            eliminar_trabajador_de_proyecto()
        elif opcion == "16":
            print("Saliendo del programa...")
            cliente.close()
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()