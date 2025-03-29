import asyncio

"""
Programa que intenta hacer cosas cool
"""


async def task1():
    """
    Esta tarea trae desde el servidor un archivo
    """
    await asyncio.sleep(2)
    return 1


async def task2():
    """
    Esta tarea tb
    """
    await asyncio.sleep(2)
    return 1


async def main():
    await asyncio.gather(*[task1(), task2()])


asyncio.run(main())
