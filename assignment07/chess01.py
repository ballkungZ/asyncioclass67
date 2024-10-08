import time

my_computer_time = 0.1
opponent_computer_time = 0.5
opponents = 10
move_pairs = 30

def game(x):
    #loops 39 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        #print(f"BOARD-{x} {i+1} Judit thinking of making a move.")
        #We think for 5 seconds
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        #The opponent thinks for 5 seconds
        time.sleep(opponent_computer_time)
        print(f"BOARD-{x+1} {i+1} Opponent made a move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} sec")
    return round(time.perf_counter() - board_start_time)
if __name__ == "__main__":
    start_time = time.perf_counter()
    #Loop 24 times because we are playing 24 opponents.
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")