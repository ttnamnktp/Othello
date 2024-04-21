from ai.heuristics.heuristic import Heuristic
from engine.GameState import GameState
from engine.Move import Move


class CornersCaptured(Heuristic):
    CAPTURED_CORNER_WEIGHT = 10
    POTENTIAL_CORNER_WEIGHT = 5
    UNLIKELY_CORNER_WEIGHT = -2

    def get_corner_value(self, game_state: GameState, player: str) -> int:
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        num_capture_corners = 0
        num_potential_corners = 0
        num_unlikely_corners = 0

        for corner in corners:
            row, col = corner
            if game_state.board[row][col] == player:
                num_capture_corners += 1

        valid_moves = Move.get_valid_moves(game_state)

        for valid_move in valid_moves:
            if valid_move in corners:
                num_potential_corners += 1

        num_unlikely_corners += len(corners) - \
            num_capture_corners - num_potential_corners

        corner_value = (num_capture_corners * CornersCaptured.CAPTURED_CORNER_WEIGHT +
                        num_potential_corners * CornersCaptured.POTENTIAL_CORNER_WEIGHT +
                        num_unlikely_corners * CornersCaptured.UNLIKELY_CORNER_WEIGHT)

        return corner_value

    def evaluate(self, game_state: GameState) -> int:
        max_player = game_state.current_player
        min_player = 'W' if max_player == 'B' else 'B'

        max_player_corner_value = self.get_corner_value(game_state, max_player)
        min_player_corner_value = self.get_corner_value(game_state, min_player)

        if (max_player_corner_value + min_player_corner_value) != 0:
            corner_heuristic_value = 100 * (max_player_corner_value - min_player_corner_value) / (
                max_player_corner_value + min_player_corner_value)
        else:
            corner_heuristic_value = 0

        return corner_heuristic_value
