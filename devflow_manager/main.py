from database import cliente
from funciones_trabajadores import eliminar_trabajador, registrar_trabajador, listar_trabajadores, actualizar_trabajador
from funciones_proyectos import crear_proyecto, eliminar_proyecto, eliminar_trabajador_de_proyecto, listar_proyectos, asignar_trabajador_a_proyecto
from funciones_tareas import crear_tarea, listar_tareas_por_proyecto, actualizar_estado_tarea
from funciones_reportes import ver_avance_proyecto, reporte_por_trabajador


def mostrar_menu_principal():
    print("\n" + "="*50)
    print("        DEVELOW MANAGER - GESTION DE PROYECTOS")
    print("="*50)
    print("1. Gestion de trabajadores")
    print("2. Gestion de proyectos")
    print("3. Gestion de tareas")
    print("4. Reportes")
    print("0. Salir")
    print("="*50)


def menu_trabajadores():
    while True:
        print("\n--- MENU TRABAJADORES ---")
        print("1. Registrar trabajador")
        print("2. Listar trabajadores")
        print("3. Actualizar trabajador")
        print("4. Eliminar trabajador")
        print("0. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            actualizar_trabajador()
        elif opcion == "4":
            eliminar_trabajador()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")


def menu_proyectos():
    while True:
        print("\n--- MENU PROYECTOS ---")
        print("1. Crear proyecto")
        print("2. Listar proyectos")
        print("3. Asignar trabajador a proyecto")
        print("4. Eliminar proyecto")
        print("0. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_proyecto()
        elif opcion == "2":
            listar_proyectos()
        elif opcion == "3":
            asignar_trabajador_a_proyecto()
        elif opcion == "4":
            eliminar_proyecto()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")


def menu_tareas():
    while True:
        print("\n--- MENU TAREAS ---")
        print("1. Crear tarea")
        print("2. Listar tareas por proyecto")
        print("3. Actualizar estado de tarea")
        print("0. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            listar_tareas_por_proyecto()
        elif opcion == "3":
            actualizar_estado_tarea()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")


def menu_reportes():
    while True:
        print("\n--- MENU REPORTES ---")
        print("1. Ver avance de proyecto")
        print("2. Generar reporte por trabajador")
        print("0. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            ver_avance_proyecto()
        elif opcion == "2":
            reporte_por_trabajador()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            menu_trabajadores()
        elif opcion == "2":
            menu_proyectos()
        elif opcion == "3":
            menu_tareas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "0":
            print("Saliendo del programa...")
            cliente.close()
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()