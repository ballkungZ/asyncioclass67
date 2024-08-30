# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    start_time = time.time()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = 0.3
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end_time = time.time()
    
    return end_time-start_time
    
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
 
# entry point coroutine
async def main():
    start_time = time.time()
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    time_1 = await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.time()
    print(f"Peoducer finished in {(time_1[0]):0.2f} seconds.")
    print(f"All finished in {round(end_time - start_time):0.2f} seconds.")
# start the asyncio program
asyncio.run(main())