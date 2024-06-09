from .Move import Move
import copy
class GameState:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.board[size // 2 - 1][size // 2 - 1] = 'W'
        self.board[size // 2][size // 2] = 'W'
        self.board[size // 2 - 1][size // 2] = 'B'
        self.board[size // 2][size // 2 - 1] = 'B'
        self.current_player = 'B'  # B: Black, W: White
        self.state_log = []  # Dictionary of state
        self.black_count = sum(row.count('B') for row in self.board)
        self.white_count = sum(row.count('W') for row in self.board)
        self.black_pass = False
        self.white_pass = False

    def flip_disks(self, move):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        opposite_player = 'W' if self.current_player == 'B' else 'B'
        for dr, dc in directions:
            r, c = move[0] + dr, move[1] + dc  # unpack the tuple
            flipped_disks = []
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == opposite_player:
                flipped_disks.append((r, c))
                r += dr
                c += dc
            if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
                for flipped_row, flipped_col in flipped_disks:
                    self.board[flipped_row][flipped_col] = self.current_player

    def is_game_over(self):
        return self.black_pass and self.white_pass

    def get_winner(self):
        # print(f"Black: {self.black_count}, White: {self.white_count}")
        if self.black_count > self.white_count:
            return 'B'
        elif self.black_count < self.white_count:
            return 'W'
        else:
            return 'Tie'

    def generate_states(self):

        # general states include states and their appropriate move
        states = []

        moves = Move.get_valid_moves(self)

        for move in moves:
            game_state = copy.deepcopy(self)
            row, col = move
            # print(move)
            # print(game_state.board)
            game_state.board[row][col] = game_state.current_player
            game_state.flip_disks(move)
            game_state.black_count = sum(row.count('B') for row in game_state.board)
            game_state.white_count = sum(row.count('W') for row in game_state.board)
            game_state.current_player = 'W' if game_state.current_player == 'B' else 'B'

            states.append([game_state, move])

        return states

    def is_terminal(self):
        moves = Move.get_valid_moves(self)
        if len(moves) == 0:
            return True
        else:
            return False
