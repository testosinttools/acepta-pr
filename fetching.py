import asyncio


"""
Programa que intenta hacer cosas cool
"""


async def task1():
    await asyncio.sleep(2)
    return 1


async def task2():
    await asyncio.sleep(2)
    return 1


async def main():
    await asyncio.gather(*[task1(), task2()])


asyncio.run(main())
