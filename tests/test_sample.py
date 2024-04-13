from engine.GameState import GameState
from engine.Move import Move


def test_sample():
    # Step 1: Initial the board
    state = GameState()
    print()

    # Step 2: Suggest valid moves
    valid_moves = Move.get_valid_moves(state)
    print(valid_moves)  # [(2, 3), (3, 2), (4, 5), (5, 4)]

    # Step 3: Choose move then update the board and flip
    print(state.current_player)
    make_move = Move.make_move(state, (2, 3))
    print(make_move)  # True

    # Step 4: Suggest valid moves
    valid_moves = Move.get_valid_moves(state)
    print(valid_moves)

    # Step 5: Choose move then update the board and flip
    print(state.current_player)
    make_move = Move.make_move(state, (4, 2))
    print(make_move)  # True

    # The board after flip
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ']
    # [' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ']
    # [' ', ' ', 'W', 'W', 'W', ' ', ' ', ' ']
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # Step 6: Suggest valid moves
    valid_moves = Move.get_valid_moves(state)
    print(valid_moves)  # (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
