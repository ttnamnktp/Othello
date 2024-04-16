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
        """Find the best move for the current player, given the available moves and depth of the search tree."""
        pass

    def evaluate(self, game_state: GameState()) -> int:
        """Evaluates the game state using a heuristic."""
        return self.heuristic.evaluate(game_state)

    def create_copy(self, game_state: GameState()) -> GameState():
        """Creates a copy of the game state."""
        game_state_copy = GameState()
        game_state_copy.board = [row[:] for row in game_state.board]
        game_state_copy.current_player = game_state.current_player
        game_state_copy.state_log = game_state.state_log[:]
        game_state_copy.white_count = game_state.white_count
        game_state_copy.black_count = game_state.black_count
        game_state_copy.black_pass = game_state.black_pass
        game_state_copy.white_pass = game_state.white_pass
        return game_state_copy
