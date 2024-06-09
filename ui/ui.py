import time

import pygame

from engine.Move import Move
from .scenes import ChessboardScene

# WIDTH = 640
# HEIGHT = 480
WIDTH = 832
# HEIGHT = 512
HEIGHT = 640

B_WIDTH = B_HEIGHT = 512  # board_width and board_height
DIMENSION = 8
SQ_SIZE = B_HEIGHT // DIMENSION  # square_size
HEIGHT_BOX = 50
WIDTH_BOX = 400
NUMBER_DEPTH = 4
WIDTH_PER_BOX = WIDTH_BOX // NUMBER_DEPTH
IMAGES = {}


def load_images():
    pieces = ['W', 'B']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(
            pygame.image.load("ui/image/" + str(piece).lower() + ".png"), (SQ_SIZE, SQ_SIZE)
        )


class ChessGUI:
    def __init__(self, gs):
        self.gs = gs
        self.selected_piece = None
        self.valid_moves = Move.check_valid_moves_and_set_pass(self.gs)
        self.running = True
        load_images()

        # Create a ChessboardScene instance
        self.chessboard_scene = ChessboardScene("Othello", gs)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    self.handle_mouse_click()

    def handle_mouse_click(self):
        x, y = pygame.mouse.get_pos()
        row = (y - (HEIGHT - B_HEIGHT) // 2) // SQ_SIZE
        col = (x - ((WIDTH - B_WIDTH) // 2) + 64) // SQ_SIZE

        if 0 <= row < DIMENSION and 0 <= col < DIMENSION:
            move = (row, col)
            if move in self.valid_moves:
                self.make_move(move)
            else:
                print("Move is invalid")
            self.selected_piece = None

    def select_piece(self, row, col):
        piece = self.gs.board[row][col]
        if piece == self.gs.current_player:
            self.selected_piece = (row, col)
            # self.valid_moves = Move.check_valid_moves_and_set_pass(self.gs)
            print(f"Valid moves: {self.valid_moves}")

    def make_move(self, move):
        Move.make_move(self.gs, move)
        self.selected_piece = None

    def run_game(self, screen):
        self.running = True
        while self.running:
            if self.gs.is_game_over():
                print("Game over")
                self.running = False  # End the game loop when the game is over
                break

            self.valid_moves = Move.check_valid_moves_and_set_pass(self.gs)
            self.draw_board(screen)
            self.highlight_valid_moves(screen)  # Highlight valid moves
            pygame.display.flip()

            if not self.valid_moves:
                continue

            self.handle_events()

    def highlight_valid_moves(self, screen):
        for move in self.valid_moves:
            row, col = move
            circle_radius = SQ_SIZE // 10
            circle_center = ((col * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64 + SQ_SIZE // 2,
                             (row * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2 + SQ_SIZE // 2)
            if self.gs.current_player == 'B':
                pygame.draw.circle(screen, pygame.Color("BLACK"), circle_center, circle_radius)
            else:
                pygame.draw.circle(screen, pygame.Color("WHITE"), circle_center, circle_radius)

    def draw_board(self, screen):
        # Call the draw method of ChessboardScene
        self.chessboard_scene.draw(screen)


class ChessBot(ChessGUI):
    def __init__(self, gs, bot):
        super().__init__(gs)
        self.bot = bot
        self.human_turn = True

    def run_game(self, screen):
        while self.running:
            if self.gs.is_game_over():
                # print("Game over")
                self.running = False
                break

            self.valid_moves = Move.check_valid_moves_and_set_pass(self.gs)
            self.draw_board(screen)
            self.highlight_valid_moves(screen)
            pygame.display.flip()

            if not self.valid_moves:
                self.human_turn = False if self.human_turn else True
                continue
            if self.human_turn:
                self.handle_events()
            else:
                self.bot_turn()

    def handle_mouse_click(self):
        if not self.human_turn:
            return
        x, y = pygame.mouse.get_pos()
        row = (y - (HEIGHT - B_HEIGHT) // 2) // SQ_SIZE
        col = (x - ((WIDTH - B_WIDTH) // 2) + 64) // SQ_SIZE
        if 0 <= row < DIMENSION and 0 <= col < DIMENSION:
            move = (row, col)
            if move in self.valid_moves:
                self.make_move(move)
                self.human_turn = False
            else:
                # print("Move is invalid")
                pass
            self.selected_piece = None

    def bot_turn(self):
        # time.sleep(0.5)
        best_move = self.bot.return_best_move(self.gs)
        Move.make_move(self.gs, best_move)
        self.human_turn = True
