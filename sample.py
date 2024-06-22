async def hi():
    print("hi")
    await hi()
    
    
async def hi():
    print("hi")

async def main():
    await hi()

import asyncio
asyncio.run(main())