import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} opponent made a move.")

    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} seconds.")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    task = []
    for i in range(opponents):
        task += [main(i)]
    await asyncio.gather(*task)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} seconds.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} seconds.")
