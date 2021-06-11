import asyncio

async def main():
    print("hello")
    await asyncio.sleep(10)
    print("world")

async def main2():
    print("how")
    await asyncio.sleep(1)
    print("are you")
    
asyncio.run(main())
asyncio.run(main2())
