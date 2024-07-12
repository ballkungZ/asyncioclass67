# example of waiting for the first task to complete
from random import random
import asyncio

#coroutine to execute in a row task
async def task_coro(dish):
    #generate a random value between 0 and 1
    time = random()+1
    #block for moment
    print(f'task :{dish} done with {time} second')
    await asyncio.sleep(time)
    return dish,time
#main coroutine
async def main():
    task = [asyncio.create_task(task_coro('rice'))
            ,asyncio.create_task(task_coro('noodle'))
            ,asyncio.create_task(task_coro('curry'))]
    
    done,pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)
    
    print("Done")
    for tasks in done:
        first_dish,time = tasks.result()
        print(f'first {first_dish} time is {time}')
    
    print("Waitting")
    for taskss in pending:
        dishs,time_ =  await taskss
        print(f'Not done first {dishs} time is {time_}')

    
#start the asyncio program 
asyncio.run(main())
