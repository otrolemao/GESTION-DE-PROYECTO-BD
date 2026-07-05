from database import proyectos, tareas, trabajadores

def ver_avance_proyecto():
    print("\n--- Avance de Proyecto ---")
    id_proyecto = input("ID del proyecto: ")
    total = tareas.count_documents({"proyecto_id": id_proyecto})
    if total == 0:
        print("No hay tareas registradas para este proyecto")
        return
    completadas = tareas.count_documents({"proyecto_id": id_proyecto, "estado": "Completada"})
    avance = (completadas / total) * 100
    print(f"Tareas completadas: {completadas}/{total}")
    print(f"Avance del proyecto: {avance:.2f}%")

def reporte_por_trabajador():
    print("\n--- Reporte por Trabajador ---")
    id_trabajador = input("ID del trabajador: ")
    trabajador = trabajadores.find_one({"_id": id_trabajador})
    if not trabajador:
        print("No se encontro el trabajador")
        return
    print(f"\nTrabajador: {trabajador['nombre']} | Rol: {trabajador['rol_principal']}")
    tareas_asignadas = list(tareas.find({"trabajador_id": id_trabajador}))
    if not tareas_asignadas:
        print("Sin tareas asignadas")
        return
    for t in tareas_asignadas:
        print(f"  - {t['nombre_tarea']} | Proyecto: {t['proyecto_id']} | Estado: {t['estado']}")
    completadas = sum(1 for t in tareas_asignadas if t["estado"] == "Completada")
    print(f"\nTotal tareas: {len(tareas_asignadas)} | Completadas: {completadas}")