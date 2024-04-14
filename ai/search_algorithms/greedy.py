import copy

from ai.heuristics.coin_parity import CoinParity
from ai.search_algorithms.search_algorithm import SearchAlgorithm
from engine.Move import Move


def create_copy(game_state):
    return copy.deepcopy(game_state)


class Greedy(SearchAlgorithm):
    """Looks ahead one move and chooses the move that maximizes the heuristic."""

    def __init__(self, heuristic=CoinParity):
        self.heuristic = heuristic()

    def find_move(self, game_state, depth=1):
        valid_moves = Move.get_valid_moves(game_state)
        best_move = valid_moves[0]
        best_score = float('-inf') if game_state.current_player == 'W' else float('inf')
        for move in valid_moves:
            next_state = create_copy(game_state)
            # next_state = game_state
            Move.make_move(next_state, move)
            score = self.heuristic.evaluate(next_state)
            compare = score >= best_score if next_state.current_player == 'W' else score < best_score
            if compare:
                best_score = score
                best_move = move
        return best_move
