from db.connection import get_connection

def agregar_departamento(nombre):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO departamentos (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        print("Departamento creado")
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()

def listar_departamentos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departamentos")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def eliminar_departamento(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM departamentos where ID = %s", (id,))
        conn.commit()
        print("Departamento eliminado")
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()
