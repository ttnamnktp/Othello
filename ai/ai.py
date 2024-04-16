from ai.search_algorithms.search_algorithm import SearchAlgorithm
from engine.GameState import GameState
from engine.Move import Move


class AI:
    """A class that uses a heuristic and search algorithm to make moves."""

    def __init__(self, heuristic, algorithm: type(SearchAlgorithm), depth):
        self.heuristic = heuristic
        self.depth = depth
        self.algorithm = algorithm(heuristic=self.heuristic)

    def return_best_move(self, game_state: GameState):
        """Returns the best move based on the current game state."""
        best_move = self.algorithm.find_move(game_state, depth=self.depth)
        return best_move

    def return_next_state(self, game_state: GameState, move):
        """Returns the new game state based on the move."""
        Move.make_move(game_state, move)
        return game_state
