from abc import ABC, abstractmethod

from engine.GameState import GameState


class Heuristic(ABC):
    """Abstract class for heuristic functions."""

    @abstractmethod
    def evaluate(self, game_state: GameState) -> int:
        """Evaluates the game state."""
        pass
