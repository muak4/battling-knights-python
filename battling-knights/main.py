import time

from game_init import app_init
from game_moves import move_knight, update_board
from game_state import generate_final_result
from utils import read_moves_file, write_json_file


def run_game():
    app_init()

    print("\n******************************************")
    print("Welcome To Battle of Knights")
    print("******************************************")

    moves = read_moves_file("moves.txt")
    update_board()

    for move in moves:
        time.sleep(1)
        move_knight(move)

    final_result = generate_final_result()
    final_result_json = write_json_file(final_result)

    print("\n******************************************")
    print("Game Over - Final Positions")
    print("******************************************")
    print(final_result_json)


if __name__ == "__main__":
    run_game()
