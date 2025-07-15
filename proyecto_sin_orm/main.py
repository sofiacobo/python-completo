import sqlite3 

conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               precio REAL NOT NULL,
               stock INTEGER NOT NULL)
""")

conn.commit()
conn.close()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import get_db

app = FastAPI()

class Producto(BaseModel): #siempre se define el tipo de dato en las clases
    nombre : str
    precio : float
    stock : int

##Definimos los enpoints
@app.post("/productos")
def crear_producto(prod: Producto): #se pasa una instancia de la clase producto
    db = get_db() #esto viene de database
    db.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (prod.nombre, prod.precio, prod.stock))
    db.commit()
    return {"mensaje": "Producto creado"}

@app.get("/productos")
def listar_productos():
    db = get_db()
    productos = db.execute("SELECT * FROM productos").fetchall()
    return [dict(p) for p in productos] #retorna un diccionario de productos 

@app.get("/productos/{id}") #traer un producto de forma individual por su id 
def obtener_producto( id:int):
    db = get_db()
    prod = db.execute("SELECT * FROM productos WHERE id = ?", (id,)).fetchone()
    if not prod:
        raise HTTPException(status_code=404,detail=" Producto no encontrado")
    return dict(prod)

@app.put("/productos/{id}") #traer un producto de forma individual por su id 
def actualizar_producto(id:int, prod : Producto): #se pasa el id y el nuevo producto a modificar(todo el producto)
    db = get_db()
    cursor = db.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?", (prod.nombre, prod.precio, prod.stock, id))
    db.commit()
    if cursor.rowcount == 0: #si no se actualiza nada entonces..
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje":"Producto actualizado"}

@app.delete("/productos/{id}")
def eliminar_producto(id:int): #se elimina buscandolo por id
    db = get_db()
    cursor = db.execute("DELETE FROM productos WHERE id = ?", (id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje":"Producto eliminado"}

