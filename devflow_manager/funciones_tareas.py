from database import tareas, proyectos, trabajadores

def crear_tarea():
    print("\n--- Crear Nueva Tarea ---")
    _id = input("ID de la tarea (ej: TA01): ")
    if tareas.find_one({"_id": _id}):
        print("ID ya existe. Por favor, elija otro.")
        return
    proyecto_id = input("ID del proyecto asociado: ")
    if not proyectos.find_one({"_id": proyecto_id}):
        print("Proyecto no encontrado.")
        return
    trabajador_id = input("ID del trabajador responsable: ")
    nombre_tarea = input("Nombre de la tarea: ")
    descripcion = input("Descripcion: ")
    prioridad = input("Prioridad (Baja/Media/Alta): ")
    fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
    estado = "Pendiente"
    documento = {
        "_id": _id,
        "proyecto_id": proyecto_id,
        "trabajador_id": trabajador_id,
        "nombre_tarea": nombre_tarea,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "fecha_limite": fecha_limite,
        "estado": estado
    }
    try:
        resultado = tareas.insert_one(documento)
        print(f"Tarea creada con ID: {resultado.inserted_id}")
    except Exception as e:
        print(f"Error al crear tarea: {e}")

def listar_tareas_por_proyecto():
    print("\n--- Listar Tareas por Proyecto ---")
    id_proyecto = input("ID del proyecto: ")
    for doc in tareas.find({"proyecto_id": id_proyecto}):
        print(f"ID: {doc['_id']} | Tarea: {doc['nombre_tarea']} | Responsable: {doc['trabajador_id']} | Estado: {doc['estado']}")

def actualizar_estado_tarea():
    print("\n--- Actualizar Estado de Tarea ---")
    id_tarea = input("ID de la tarea: ")
    nuevo_estado = input("Nuevo estado (Pendiente/En progreso/Completada/Bloqueada): ")
    resultado = tareas.update_one(
        {"_id": id_tarea},
        {"$set": {"estado": nuevo_estado}}
    )
    if resultado.modified_count > 0:
        print("Estado actualizado correctamente")
    else:
        print("No se encontro la tarea")

def eliminar_tarea():
    for doc in tareas.find():
        print("--------------------------------------------------")
        print(f"ID: {doc['_id']} | Tarea: {doc['nombre_tarea']} | Responsable: {doc['trabajador_id']} | Estado: {doc['estado']}")
        print("--------------------------------------------------")
    print("\n--- Eliminar Tarea ---")
    id_tarea = input("ID de la tarea a eliminar: ")
    resultado = tareas.delete_one({"_id": id_tarea})
    if resultado.deleted_count > 0:
        print("Tarea eliminada correctamente")
    else:
        print("No se encontro la tarea")
