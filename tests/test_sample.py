from engine.GameState import GameState
from engine.Move import Move


def print_state(state):
    for row in state.board:
        print(row)
    print("Current Player:", state.current_player)

# 1. Check is end game
# 2. Suggest valid moves and set pass
# 3. Choose move then update the board and flip


def test_sample():
    # Step 1: Initial the board
    state = GameState()
    print(" ")
    print("-----------------------------------")
    print_state(state)

    # Step 2: Check is end game
    print(state.is_game_over())

    # Step 3: Suggest valid moves
    valid_moves = Move.check_valid_moves_and_set_pass(state)
    print(valid_moves)

    # Step 4: Choose move then update the board and flip
    make_move = Move.make_move(state, (2, 3))
    print("-----------------------------------")
    print_state(state)

    # Step 5: Check is end game
    print(state.is_game_over())

    # Step 6: Suggest valid moves
    valid_moves = Move.check_valid_moves_and_set_pass(state)
    print(valid_moves)

    # Step 6: Choose move then update the board and flip
    make_move = Move.make_move(state, (4, 2))
    print("-----------------------------------")
    print_state(state)

    # Step 7: undo move
    undo_move = Move.undo_move(state)
    print("-----------------------------------")
    print(undo_move)
    print_state(state)
