from models.departamentos import agregar_departamento, eliminar_departamento, listar_departamentos
from models.empleados import agregar_empleado, listar_empleados


def menu():
    while True:

        print("\n---Sistema de Gestion de empleados y departamentos ---")
        print("1. Agregar Empleado")
        print("2. Listar Empleados")
        print("3. Agregar Departamento")
        print("4. Listar Departamentos")
        print("5. Eliminar Departamento")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            salario = float(input("Salario: "))
            fecha = input("Fecha ingreso (YYYY-MM-DD): ")
            id_dpto = int(input("ID del departamento: "))
            agregar_empleado(nombre,email,salario,fecha,id_dpto)
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            nombre = input("Nombre del departamento: ")
            agregar_departamento(nombre)
        elif opcion == "4":
            listar_departamentos()
        elif opcion == "5":
            id = int(input("ID del departamento:"))
            eliminar_departamento(id)
        elif opcion == "6":
            print("Hasta luego!")
            break    
        else:
            print("Opcion no valida")
        
menu()
