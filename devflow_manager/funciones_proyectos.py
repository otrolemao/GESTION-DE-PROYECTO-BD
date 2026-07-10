from database import proyectos, trabajadores

def crear_proyecto():
    print("\n--- Crear Nuevo Proyecto ---")
    _id = input("ID del proyecto (ej: P01): ")
    if proyectos.find_one({"_id": _id}):
        print("ID ya existe. Por favor, elija otro.")
        return
    nombre = input("Nombre del proyecto: ")
    if not _id.startswith("P") or not _id[1:].isdigit():
        print("ID inválido. Debe comenzar con 'P' seguido de números (ej: P01).")
        return
    descripcion = input("Descripcion: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin_estimada = input("Fecha de fin estimada (YYYY-MM-DD): ")
    estado = "Planificacion"
    equipo_ids = input("IDs de trabajadores separados por coma (ej: T01,T02): ").split(",")
    equipo_ids = [id.strip() for id in equipo_ids if id.strip()]
    documento = {
        "_id": _id,
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_inicio": fecha_inicio,
        "fecha_fin_estimada": fecha_fin_estimada,
        "estado": estado,
        "equipo_ids": equipo_ids
    }
    try:
        resultado = proyectos.insert_one(documento)
        print(f"Proyecto creado con ID: {resultado.inserted_id}")
    except Exception as e:
        print(f"Error al crear proyecto: {e}")

def listar_proyectos():
    print("\n--- Listado de Proyectos ---")
    for doc in proyectos.find():
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Estado: {doc['estado']} | Inicio: {doc['fecha_inicio']}")

def asignar_trabajador_a_proyecto():
    for doc in trabajadores.find():
        print(" Lista trabajadores:")
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Rol: {doc['rol_principal']} | Estado: {doc['estado']}")
        print("--------------------------------------------------")
    for doc in proyectos.find():
        print(" Lista proyectos:")
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Estado: {doc['estado']} | Inicio: {doc['fecha_inicio']}")
        print("--------------------------------------------------")
    print("\n--- Asignar Trabajador a Proyecto ---")
    id_proyecto = input("ID del proyecto: ")
    id_trabajador = input("ID del trabajador a agregar: ")
    resultado = proyectos.update_one(
        {"_id": id_proyecto},
        {"$addToSet": {"equipo_ids": id_trabajador}}
    )
    if resultado.modified_count > 0:
        print("Trabajador asignado al proyecto")
    else:
        print("No se encontro el proyecto o el trabajador ya estaba asignado")


def eliminar_proyecto():
    for doc in proyectos.find():
        print("--------------------------------------------------")
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Estado: {doc['estado']} | Inicio: {doc['fecha_inicio']}")
        print("--------------------------------------------------")
        print("\n--- Eliminar Proyecto ---")
    id_proyecto = input("ID del proyecto a eliminar: ")
    resultado = proyectos.delete_one({"_id": id_proyecto})
    if resultado.deleted_count > 0:
        print("Proyecto eliminado correctamente")
    else:
        print("No se encontro el proyecto")
        
