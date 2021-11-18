import time
import game_grid as gr
from game_class import Game
from minimax import minimax
from alphabeta import alphabeta

TEST_1_SCORE = 16
TEST_2_SCORE = 19


def print_moves(moves):
    moves.reverse()
    grids = []
    for game in moves:
        grids.append(game.get_grid())
    for move in grids:
        print("~~~~~~~~~~~~~~~~~~")
        for m in move:
            print(m)


def print_last_move(moves):
    grids = []
    for game in moves:
        grids.append(game.get_grid())
    for move in grids[0]:
            print(move)


def init_game_minimax(grid=1):
    grid = gr.create_grid(grid)
    start_location = gr.get_start_location()
    game = Game(grid, start_location)
    score, moves = minimax(game)
    if score < game.max_steps():
        print("Score:", score)
    else:
        print("Score: infinity")
    return score, moves
    # print_last_move(moves)


def init_game_alphabeta(grid=1):
    grid = gr.create_grid(grid)
    start_location = gr.get_start_location()
    game = Game(grid, start_location)
    score, moves = alphabeta(game)
    if score < game.max_steps():
        print("Score:", score)
    else:
        print("Score: infinity")
    return score, moves


def test_minimax(game=1, print_all_moves=False, print_last=False):
    start_time = time.time()
    score, moves = init_game_minimax(game)  # If you want to test your algorithm on grid_2 - change the paramater to 2
    print("Running time: %s seconds" % (time.time() - start_time))
    if print_all_moves:
        print_moves(moves)
    if print_last:
        print_last_move(moves)
    return score

def test_alphabeta(game=1, print_all_moves=False, print_last=False):
    start_time = time.time()
    score, moves = init_game_alphabeta(game)
    print("Running time: %s seconds" % (time.time() - start_time))
    if print_all_moves:
        print_moves(moves)
    if print_last:
        print_last_move(moves)
    return score


"""
Testing minimax vs alphabeta, including running time comparison
To print all game boards of a specific algorithm, you may use the function: print_moves(moves) 
To print only the last move, you may use the function: print_last_move(moves)
"""

print("Testing the algorithms")
print("If you want to print the game board, change the parameters print_all_moves or print_last to True\n")
print("--- Test 1 minimax ---")
test_1 = "Passed" if test_minimax(1, print_all_moves=False, print_last=False) == TEST_1_SCORE else "Failed"
print("--- Test 1 alphabeta ---")
test_1_ab = "Passed" if test_alphabeta(1, print_all_moves=False, print_last=False) == TEST_1_SCORE else "Failed"
print('Minimax test 1: ', test_1)
print('Alphabeta test 1: ', test_1_ab)

print("--- Test 2 minimax ---")
test_2 = "Passed" if test_minimax(2, print_all_moves=False, print_last=False) == TEST_2_SCORE else "Failed"
print("--- Test 2 alphabeta ---")
test_2_ab = "Passed" if test_alphabeta(2, print_all_moves=False, print_last=False) == TEST_2_SCORE else "Failed"
print('Minimax test 2: ', test_2)
print('Alphabeta test 2: ', test_2_ab)
