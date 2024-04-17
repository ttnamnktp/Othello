import random
import time

from ai.search_algorithms.search_algorithm import SearchAlgorithm
from engine.GameState import GameState
from engine.Move import Move


class MinimaxAlphaBeta(SearchAlgorithm):
    """Implements the Minimax algorithm with Alpha-Beta pruning."""

    def find_move(self, game_state: GameState, depth: int) -> (int, int):
        self.start_time = time.time()
        best_score = float('-inf') if game_state.current_player == 'W' else float('inf')
        best_move = None
        candidate_best_move = []
        for move in Move.get_valid_moves(game_state):
            next_state = self.create_copy(game_state)
            Move.make_move(next_state, move)
            score = self.minimax(next_state, depth, game_state.current_player == 'W', float('-inf'), float('inf'))
            compare = score < best_score if next_state.current_player == 'W' else score > best_score
            if compare:
                best_score = score
                best_move = move
                candidate_best_move.clear()
                candidate_best_move.append(move)
            else:
                candidate_best_move.append(move)
        if candidate_best_move:
            best_move = random.choice(candidate_best_move)
        return best_move

    def minimax(self, game_state: GameState, depth: int, is_maximizing: bool, alpha: float, beta: float) -> int:
        """Minimax algorithm with Alpha-Beta pruning.
        Prunes the tree by eliminating branches that cannot possibly improve the result.
        Stops searching after reaching the maximum depth or when the game is over or after the run time limit.
        """
        if depth == 0 or game_state.is_game_over() or time.time() - self.start_time > self.run_time:
            return self.evaluate(game_state)

        if is_maximizing:
            best_score = float('-inf')
            for move in Move.get_valid_moves(game_state):
                next_state = self.create_copy(game_state)
                Move.make_move(next_state, move)
                score = self.minimax(next_state, depth - 1, False, alpha, beta)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in Move.get_valid_moves(game_state):
                next_state = self.create_copy(game_state)
                Move.make_move(next_state, move)
                score = self.minimax(next_state, depth - 1, True, alpha, beta)
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
