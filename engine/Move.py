class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def get_valid_moves(game_state):
        valid_moves = []
        for i in range(game_state.size):
            for j in range(game_state.size):
                if Move.is_valid_move(game_state, i, j):
                    valid_moves.append((i, j))
        return valid_moves

    @staticmethod
    def is_valid_move(game_state, row, col):
        if game_state.board[row][col] != ' ':
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        opposite_player = 'W' if game_state.current_player == 'B' else 'B'
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < game_state.size and 0 <= c < game_state.size and game_state.board[r][c] == opposite_player:
                r += dr
                c += dc
                while 0 <= r < game_state.size and 0 <= c < game_state.size and game_state.board[r][
                        c] == opposite_player:
                    r += dr
                    c += dc
                if 0 <= r < game_state.size and 0 <= c < game_state.size and game_state.board[r][
                        c] == game_state.current_player:
                    return True
        return False

    @staticmethod
    def make_move(game_state, move):
        row, col = move  # unpack the tuple
        if Move.is_valid_move(game_state, row, col):
            game_state.board[row][col] = game_state.current_player
            game_state.flip_disks(move)
            game_state.current_player = 'W' if game_state.current_player == 'B' else 'B'
            return True
        else:
            return False
