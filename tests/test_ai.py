from ai.ai import AI
from ai.heuristics.coin_parity import CoinParity
from ai.search_algorithms.greedy import Greedy
from ai.search_algorithms.random import Random
from engine.GameState import GameState
from engine.Move import Move


def print_state(state):
    for row in state.board:
        print(row)
    print("Current Player:", state.current_player)
    suggest_move(state)


def print_current_move(state, move):
    print(f"{state.current_player}:", move)


def suggest_move(state):
    print(f"Available moves: {Move.get_valid_moves(state)}")


def ai_plays_itself(ai: AI):
    """Test the AI by making it play against itself."""
    state = GameState()
    print()

    print("Initial State")
    print_state(state)
    while not state.is_game_over():
        best_move = ai.return_best_move(state)
        print_current_move(state, best_move)
        print_state(state=ai.return_next_state(state, best_move))
    print("Game Over")


def test_sample():
    random_ai = AI(heuristic=CoinParity(), algorithm=Random(), depth=1)
    greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy(), depth=1)
    ai_plays_itself(ai=random_ai)
