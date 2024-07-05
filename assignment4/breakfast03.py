# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: wating...")
    await asyncio.sleep(5)  #2:pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs(): #1
    start = time()
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)
    print("eggs: ready")
    print(f"fry_eggs is ready in {time()-start} min")

async def main(): #1
    start = time()
    coffee_task = asyncio.create_task(make_coffee())
    fryeggs_task = asyncio.create_task(fry_eggs())
    await coffee_task #run task wait await
    await fryeggs_task
    print(f"breakfast is ready in {time()-start} min")

asyncio.run(main()) #runtop-level function concurrently
