from ai.heuristics.heuristic import Heuristic

from abc import ABC

from ai.heuristics.heuristic import Heuristic
from engine.GameState import GameState


class HybridHeuristic(Heuristic, ABC):
    """Evaluates the board based on the difference in the number of coins of each color
    and the position of each coin take place."""

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

    def evaluate(self, game_state: GameState) -> int:

        # define weight of black and white coin and alpha
        black_weight = 0
        white_weight = 0
        max_weight = 0
        alpha = 0.5 # weight parameter

        # calculate max value of the weight, the weight of black and white coin
        for i in range(game_state.size):
            for j in range(game_state.size):
                if game_state.board[i][j] == 'B':
                    black_weight += HybridHeuristic.STATIC_WEIGHT[i][j]
                    max_weight += abs(HybridHeuristic.STATIC_WEIGHT[i][j])
                elif game_state.board[i][j] == 'W':
                    white_weight += HybridHeuristic.STATIC_WEIGHT[i][j]
                    max_weight += abs(HybridHeuristic.STATIC_WEIGHT[i][j])

        # calculate each component of hybrid function
        coin_parity = 100 * (game_state.white_count - game_state.black_count) / (game_state.white_count + game_state.black_count)
        weight_matrix = 100 * (white_weight - black_weight) / max_weight

        # sum of two component
        hybrid = (alpha * coin_parity) + ((1 - alpha) * weight_matrix)

        return int(hybrid)


class DynamicHybridHeuristic(Heuristic, ABC):
    """Evaluates the board based on the difference in the number of coins of each color
    and the position of each coin take place."""

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

    def evaluate(self, game_state: GameState) -> int:

        # define weight of black and white coin and alpha
        black_weight = 0
        white_weight = 0
        max_weight = 0
        alpha = 0 # weight parameter

        # calculate max value of the weight, the weight of black and white coin
        for i in range(game_state.size):
            for j in range(game_state.size):
                if game_state.board[i][j] == 'B':
                    black_weight += HybridHeuristic.STATIC_WEIGHT[i][j]
                    max_weight += abs(HybridHeuristic.STATIC_WEIGHT[i][j])
                elif game_state.board[i][j] == 'W':
                    white_weight += HybridHeuristic.STATIC_WEIGHT[i][j]
                    max_weight += abs(HybridHeuristic.STATIC_WEIGHT[i][j])

        # calculate each component of hybrid function
        coin_parity = 100 * (game_state.white_count - game_state.black_count) / (game_state.white_count + game_state.black_count)
        weight_matrix = 100 * (white_weight - black_weight) / max_weight

        # calculate alpha
        coin_numbers = game_state.white_count + game_state.black_count
        move_numbers = coin_numbers - 4
        minimum_alpha = 0.4 # minimum value of alpha
        maximum_alpha = 0.7 # maximum value of alpha
        polynomial_degree = 5 # bigger polynominal degree, slower alpha changes at the beginning of the game
        gamma = (maximum_alpha - minimum_alpha)/(60**polynomial_degree)
        alpha = gamma * move_numbers**polynomial_degree + minimum_alpha
        #alpha chạy từ 0 đến 1

        # sum of two component
        hybrid = (alpha * coin_parity) + ((1 - alpha) * weight_matrix)

        return int(hybrid)
