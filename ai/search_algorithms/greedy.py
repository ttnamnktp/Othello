import random

from ai.search_algorithms.search_algorithm import SearchAlgorithm
from engine.Move import Move


class Greedy(SearchAlgorithm):
    """Looks ahead one move and chooses the move that maximizes the heuristic."""

    def find_move(self, game_state, depth=1):
        candidate_best_move = []
        valid_moves = Move.get_valid_moves(game_state)
        best_move = None
        best_score = float('-inf') if game_state.current_player == 'W' else float('inf')
        for move in valid_moves:
            next_state = self.create_copy(game_state)
            Move.make_move(next_state, move)
            score = self.evaluate(next_state)
            compare = score <= best_score if next_state.current_player == 'W' else score >= best_score
            if compare:
                best_score = score
                candidate_best_move.append(move)
        if candidate_best_move:  # Check if the list is not empty
            best_move = random.choice(candidate_best_move)
        return best_move
