from sympy import re

from database import trabajadores

def registrar_trabajador():
    print("\n--- Registrar Nuevo Trabajador ---")
    _id = input("ID del trabajador (ej: T01): ")\
    
    if trabajadores.find_one({"_id": _id}):
        print("ID ya existe. Por favor, elija otro.")
        return     
    
    if not _id.startswith("T") or not _id[1:].isdigit():
        print("ID inválido. Debe comenzar con 'T' seguido de números (ej: T01).")
        return
    
    nombre = input("Nombre completo: ")
    correo = input("Correo: ")
    rol_principal = input("Rol principal (Backend/Frontend/QA/UX/Scrum Master): ")
    especialidad = input("Especialidad: ")
    estado = "Activo"
    documento = {
        "_id": _id,
        "nombre": nombre,
        "correo": correo,
        "rol_principal": rol_principal,
        "especialidad": especialidad,
        "estado": estado
    }
    try:
        resultado = trabajadores.insert_one(documento)
        print(f"Trabajador registrado con ID: {resultado.inserted_id}")
    except Exception as e:
        print(f"Error al registrar trabajador: {e}")

def listar_trabajadores():
    print("\n--- Listado de Trabajadores ---")
    for doc in trabajadores.find():
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Rol: {doc['rol_principal']} | Estado: {doc['estado']}")

def actualizar_trabajador():
    print("\n--- Actualizar Trabajador ---")
    _id = input("ID del trabajador a actualizar: ")
    nuevo_rol = input("Nuevo rol principal: ")
    nueva_especialidad = input("Nueva especialidad: ")
    resultado = trabajadores.update_one(
        {"_id": _id},
        {"$set": {"rol_principal": nuevo_rol, "especialidad": nueva_especialidad}}
    )
    if resultado.modified_count > 0:
        print("Trabajador actualizado correctamente")
    else:
        print("No se encontro el trabajador o no hubo cambios")
        
def eliminar_trabajador():
    for doc in trabajadores.find():
        print("--------------------------------------------------")
        print(f"ID: {doc['_id']} | Nombre: {doc['nombre']} | Rol: {doc['rol_principal']} | Estado: {doc['estado']}")
        print("--------------------------------------------------")
    print("\n--- Eliminar Trabajador ---")
    _id = input("ID del trabajador a eliminar: ")
    resultado = trabajadores.delete_one({"_id": _id})
    if resultado.deleted_count > 0:
        print("Trabajador eliminado correctamente")
    else:
        print("No se encontro el trabajador")



