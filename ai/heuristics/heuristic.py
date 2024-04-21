from abc import ABC, abstractmethod

from engine.GameState import GameState


class Heuristic(ABC):
    """Abstract class for heuristic functions.
    A heuristic class has its own way of evaluating a game state.
    """

    STATIC_WEIGHT = [
        [4, -3, 2, 2, 2, 2, -3, 4],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [4, -3, 2, 2, 2, 2, -3, 4]
    ]

    @abstractmethod
    def evaluate(self, game_state: GameState) -> int:
        """Evaluates the game state."""
        pass
