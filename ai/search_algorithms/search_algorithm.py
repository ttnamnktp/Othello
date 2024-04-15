import copy
from abc import ABC, abstractmethod

from engine.GameState import GameState


class SearchAlgorithm(ABC):
    """Abstract class for search algorithms.
    Each search algorithm will search in the game tree for the best move.
    With each move made, it will generate a new game state and continue searching.
    When it reaches the maximum depth, it will evaluate the game state using a heuristic function.
    """

    def __init__(self, heuristic=None):
        """Initializes the search algorithm with a heuristic function."""
        self.heuristic = heuristic

    @abstractmethod
    def find_move(self, game_state: GameState(), depth: int) -> (int, int):
        """Find the best move for the current player, given the current state of the board and how far it looks into
        the future."""
        pass

    @abstractmethod
    def evaluate(self, game_state: GameState()) -> int:
        """Evaluates the game state."""
        pass

    def create_copy(self, game_state: GameState()) -> GameState():
        """Creates a deep copy of the game state."""
        return copy.deepcopy(game_state)
