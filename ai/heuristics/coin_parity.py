from ai.heuristics.heuristic import Heuristic


class CoinParity(Heuristic):
    """Evaluates the board based on the difference in the number of coins of each color."""

    def evaluate(self, game_state) -> int:
        return int(
            100 * (game_state.white_count - game_state.black_count) / (game_state.white_count + game_state.black_count))
