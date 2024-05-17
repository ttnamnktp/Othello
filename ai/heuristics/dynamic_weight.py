from ai.heuristics.heuristic import Heuristic

from abc import ABC

from ai.heuristics.heuristic import Heuristic
from engine.GameState import GameState


class DynamicWeight(Heuristic, ABC):
    """Evaluates the board based on the difference in the number of coins of each color
    and the position of each coin take place."""

    STATIC_WEIGHT = [
        [16, -6, 4, 4, 4, 4, -6, 16],
        [-6, -16, -2, -2, -2, -2, -16, -6],
        [4, -2, 2, 0, 0, 2, -2, 4],
        [4, -2, 0, 2, 2, 0, -2, 4],
        [4, -2, 0, 2, 2, 0, -2, 4],
        [4, -2, 2, 0, 0, 2, -2, 4],
        [-6, -16, -2, -2, -2, -2, -16, -6],
        [16, -6, 4, 4, 4, 4, -6, 16],
    ]

    # average weight difference matrix
    average_weight_difference = None

    # dynamic weight matrix change by number of made moves
    dynamic_weight = None

    def set_average_weight_difference(self, game_state: GameState):

        matrix_size = game_state.size
        total_score = 0

        for i in range(matrix_size):
            for j in range(matrix_size):
                total_score += self.STATIC_WEIGHT[i][j]

        average_score = total_score / (matrix_size**2)
        average_difference = [[0 for _ in range(0,matrix_size)] for _ in range(0,matrix_size)]

        for i in range(game_state.size):
            for j in range(game_state.size):
                average_difference[i][j] = average_score - self.STATIC_WEIGHT[i][j]

        # print(average_difference)
        self.average_weight_difference = average_difference

    def evaluate(self, game_state: GameState) -> int:

        # calculate average_weight matrix
        matrix_size = game_state.size
        self.set_average_weight_difference(game_state)

        # calculate new dynamic weight matrix
        temp_dynamic_weight = self.STATIC_WEIGHT
        coin_numbers = game_state.white_count + game_state.black_count
        made_move_numbers = coin_numbers - 4
        maximum_move_numbers = game_state.size**2 - 4

        for iteration in range(0, made_move_numbers):
            for i in range(game_state.size):
                for j in range(game_state.size):
                    temp_dynamic_weight[i][j] += \
                        (4 * iteration**3 * self.average_weight_difference[i][j])/((maximum_move_numbers*(maximum_move_numbers-1))**2)

        self.dynamic_weight = temp_dynamic_weight


        # print(self.dynamic_weight)

        # calculate max value of the weight, the weight of black and white coin

        black_weight = 0
        white_weight = 0
        max_weight = 0

        for i in range(game_state.size):
            for j in range(game_state.size):
                if game_state.board[i][j] == 'B':
                    black_weight += self.dynamic_weight[i][j]
                    max_weight += abs(self.dynamic_weight[i][j])
                elif game_state.board[i][j] == 'W':
                    white_weight += self.dynamic_weight[i][j]
                    max_weight += abs(self.dynamic_weight[i][j])

        # calculate

        return white_weight - black_weight
