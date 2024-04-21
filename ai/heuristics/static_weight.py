from abc import ABC

from ai.heuristics.heuristic import Heuristic
from engine.GameState import GameState


class StaticWeight(Heuristic, ABC):
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
        cur_player_weight = 0
        for i in range(game_state.size):
            for j in range(game_state.size):
                if game_state.board[i][j] == game_state.current_player:
                    cur_player_weight += self.STATIC_WEIGHT[i][j]

        return cur_player_weight
