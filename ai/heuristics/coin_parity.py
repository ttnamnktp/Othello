from ai.heuristics.heuristic import Heuristic
from engine.GameState import GameState


class CoinParity(Heuristic):
    """Evaluates the board based on the difference in the number of coins of each color."""

    def evaluate(self, game_state: GameState) -> int:
        board = game_state.board
        num_black_coins = sum(row.count('B') for row in board)
        num_white_coins = sum(row.count('W') for row in board)
        return int(100 * (num_white_coins - num_black_coins) / (num_white_coins + num_black_coins))


if __name__ == "__main__":
    game_state = GameState()
    coin_parity = CoinParity()
    print(coin_parity.evaluate(game_state))
