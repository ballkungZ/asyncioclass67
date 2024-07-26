import time
import asyncio

my_computer_time = 0.1
opponent_computer_time = 0.5
opponents = 24
move_pairs = 30

#Again notice that I declare the main() function as a async function
async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_computer_time)
        print(f"BOARD-{x} {i+1} Judit made a move.")
        time.sleep(opponent_computer_time)
        print(f"BOARD-{x} {i+1} Opponent made a move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter())}")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    #Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f'Board exhibition finished in {round(time.perf_counter() - start_time)} secs')
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")