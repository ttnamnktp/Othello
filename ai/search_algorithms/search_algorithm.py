from abc import ABC, abstractmethod

from engine.GameState import GameState


class SearchAlgorithm(ABC):
    """Abstract class for search algorithms."""

    @abstractmethod
    def find_move(self, game_state: GameState(), depth: int) -> (int, int):
        """Find the best move for the current player, given the current state of the board and how far it looks into
        the future."""
        pass
