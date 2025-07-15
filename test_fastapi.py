from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# # app = FastAPI()

# # @app.get("/")
# # def read_root():
# #     return {"mensaje": "Hola FastAPI"}

# # # @app.get("/item/{item_id}") #podria ser el id de algun usuario
# # # def read_item(item_id: int, query_param: str = None ):
# # #     return {"item_id": item_id, "query_params": query_param}

# # class Item(BaseModel): #esto es como crear una clase articulo
# #     name: str
# #     price: float
# #     is_offer: bool = False

# # @app.put("/item/{item_id}")
# # def update_item(item_id : int, item: Item):
# #     return {"item_id": item_id, "item_name": item.name}

# # @app.get("/item/{item_id}")
# # def read_item(item_id : int):
# #     if item_id == 0: #con esto hacemos manejo de errores
# #         raise HTTPException(status_code=404, detail="El item no se encuentra")
# #     return {"item_id": item_id}


#------------------------------------------------------------------------------------------------#

app = FastAPI(title="API de gestion de tareas")

# Modelo de datos
class Tarea(BaseModel):
    titulo : str
    descripcion: str
    completada: bool = False #por default queda en falso

tareas : List[Tarea] = []

# #Aqui empezamos a crear nuestras rutas
#Crear una tarea
@app.post("/tareas", response_model = Tarea)
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

# Listar tareas
@app.get("/tareas", response_model = List[Tarea]) #el response model es como quiero que sea la respuesta, en este caso quiero que me devuelva una lista de tareas
def listar_tareas():
    return tareas

# Ver una tarea en especifico
@app.get("/tareas/{id}", response_model = Tarea)
def obtener_tarea(id: int):
    if id < 0 or id >= len(tareas): #verifico si esta en la lista o no
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas[id]

# Actualizar tarea a completada
@app.put("/tareas/{id}/completar", response_model = Tarea)
def completar_tarea(id:int): #le paso el id de la tarea que se va a completar
    if id < 0 or id >= len(tareas): #verifico si esta en la lista o no
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tareas[id].completada = True #cambio el valor del atributo a true
    return tareas[id]

# Eliminar tarea
@app.delete("/tareas/{id}")
def eliminar_tarea(id:int): #le pasamos el id de la tarea que se va a eliminar
    if id < 0 or id >= len(tareas): #verifico si esta en la lista o no
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_eliminada = tareas.pop(id) #con pop se elimina la tarea
    return {"mensaje": "Tarea eliminada", "tarea eliminada": tarea_eliminada}