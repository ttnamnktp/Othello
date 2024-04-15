import random

from ai.search_algorithms.search_algorithm import SearchAlgorithm
from engine.GameState import GameState
from engine.Move import Move


class Random(SearchAlgorithm):
    """Chooses a random move."""

    def find_move(self, game_state, depth=1):
        valid_moves = Move.get_valid_moves(game_state)
        return random.choice(valid_moves)

    def evaluate(self, game_state: GameState()) -> int:
        pass
