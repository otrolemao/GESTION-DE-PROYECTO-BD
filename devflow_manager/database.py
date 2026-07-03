import pymongo
import pymongo.errors

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO = 1000
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"
MONGO_BD = "devflow"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=MONGO_TIEMPO)
    db = cliente[MONGO_BD]
    trabajadores = db["trabajadores"]
    proyectos = db["proyectos"]
    tareas = db["tareas"]
    print("Conexion exitosa a MongoDB")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Tiempo excedido: {error}")
    exit()
except pymongo.errors.ConnectionFailure as error:
    print(f"Fallo al conectarse a MongoDB: {error}")
    exit()