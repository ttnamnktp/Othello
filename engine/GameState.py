from .Move import Move


class GameState:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.board[size // 2 - 1][size // 2 - 1] = 'W'
        self.board[size // 2][size // 2] = 'W'
        self.board[size // 2 - 1][size // 2] = 'B'
        self.board[size // 2][size // 2 - 1] = 'B'
        self.current_player = 'B'  # B: Black, W: White
        self.move_log = []

    def undo_move(self):
        if len(self.move_log) == 0:
            return False
        self.current_player = 'B' if self.current_player == 'W' else 'W'
        self.board = self.move_log[-2]

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
        return len(Move.get_valid_moves(self)) == 0
