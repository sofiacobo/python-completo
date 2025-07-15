from db.connection import get_connection
from services.validar_email import validar_email

def agregar_empleado(nombre,email,salario,fecha_ingreso,departamento_id):
    if not validar_email(email):
        print("Email inválido")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO empleados (nombre,email,salario,fecha_ingreso,departamento_id) 
                       VALUES (%s, %s, %s, %s, %s)""", 
                       (nombre,email,salario,fecha_ingreso,departamento_id))
        conn.commit()
        print("Empleado agregado con éxito")
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()

def listar_empleados():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT e.id, e.nombre, e.email, e.salario, e.fecha_ingreso, d.nombre AS Departamento
    FROM empleados e
    LEFT JOIN departamentos d ON e.departamento_id = d.id
    """
    cursor.execute(query)
    for e in cursor.fetchall():
        print(e)
    cursor.close()
    conn.close()

def modificar_salario_empleado():
    pass

def eliminar_empleado():
    pass

# def eliminar_departamento(id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("DELETE FROM departamentos where ID = %s", (id,))
#         conn.commit()
#         print("Departamento eliminado")
#     except Exception as e:
#         print("Error: ", e)
#     finally:
#         cursor.close()
#         conn.close()