# import mysql.connector
# from dotenv import load_dotenv
# import os 

# load_dotenv()

# # se abre la conexion a la bd y se llaman a las variables de entorno
# conn = mysql.connector.connect(
#     host = os.getenv("DB_HOST"),
#     user = os.getenv("DB_USER"),
#     password = os.getenv("DB_PASS"),
#     database = os.getenv("DB_NAME")
# )

# print("Conexion OK")
# cursor = conn.cursor()

#SENTENCIA PARA LECTURA DE DATOS
# cursor.execute("SELECT * FROM empleados;")
# print("Ejecucion consulta OK")
# for row in cursor.fetchall():
#     print(row)

# INSERCION DE DATOS
# sql = "INSERT INTO empleados (nombre, puesto, sueldo) VALUES (%s,%s,%s)"
# data = ("Juan", "Gerente", 5000)
# cursor.execute(sql, data)

# #commiteamos los cambios para que se guarde en la base
# conn.commit()

## Manejo de errores
# try:
#     conn = mysql.connector.connect(
#         host = os.getenv("DB_HOST"),
#         user= os.getenv("DB_USER"),
#         password = os.getenv("DB_PASS"),
#         database = os.getenv("DB_NAME")
#     )

#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM empleados WHERE sueldo > 3000;")
#     for row in cursor.fetchall():
#         print(row)
# except mysql.connector.Error as err:
#     print("Error:", err)

# finally:
#     cursor.close()
#     conn.close()

# Transacciones -> conjunto de operaciones sql, se completan todas bien o no se ejecuta ninguna
# try:
#     conn.start_transaction()
#     cursor.execute("UPDATE empleados SET sueldo = sueldo * 1.1 WHERE puesto = 'Analista'")
#     cursor.execute("INSERT INTO empleados(nombre,puesto,sueldo) VALUES ('Error','Interno',bad)") # Generar un error
#     conn.commit()
# except Exception as e: #el error no se commitea
#     print("Revirtiendo cambios", e)
#     conn.rollback() #todo vuelve al estado anterior al start transaction

