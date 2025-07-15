# import time

# def tarea(id):
#     print(f"Inicio tarea {id}")
#     time.sleep(5)
#     print(f"Fin tarea {id}")

# def main():
#     for i in range(3):
#         tarea(i)

# main()

import asyncio

async def tarea(id):
    print(f"Inicio tarea {id}")
    await asyncio.sleep(5) #await para funciones asincronas
    print(f"Fin tarea {id}")

async def main():
    await asyncio.gather(tarea(1), tarea(2), tarea(3)) #las tres tareas se ejecutan asincronamente (al mismo tiempo)

asyncio.run(main())