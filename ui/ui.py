import pygame
from engine.GameState import GameState as gs

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


class SimpleScene:
    def __init__(self, text):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.text = text

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 80)
        text = font.render(self.text, True, pygame.Color(144, 8, 8))
        textRect = text.get_rect()
        # textRect.center = (WIDTH // 2, HEIGHT // 3)
        textRect.center = (WIDTH // 2, HEIGHT // 5)

        screen.blit(text, textRect)
        play = pygame.transform.scale(pygame.image.load("ui/image/start.png"), (
            pygame.image.load("UI/image/start.png").get_width() // 6,
            pygame.image.load("UI/image/start.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(play, self.playRect)

        help = pygame.transform.scale(pygame.image.load("ui/image/help.png"), (
            pygame.image.load("UI/image/help.png").get_width() // 9,
            pygame.image.load("UI/image/help.png").get_height() // 9))
        self.helpRect = help.get_rect()
        self.helpRect.center = (WIDTH // 2, HEIGHT // 1.25)
        screen.blit(help, self.helpRect)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    return ('CHOOSE_MODE')
                elif self.helpRect.collidepoint(event.pos):
                    return 'HELP'
        return None

    def element(self, events):
        pass


class HelpScene:
    def __init__(self, title, *texts):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.texts = texts
        self.title = title

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 1

        for text in self.texts:
            font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, (HEIGHT // 8 + HEIGHT // 5 * n))
            screen.blit(text, textRect)
            n += 1

        font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 40)
        text = font.render(self.title, True, pygame.Color(144, 8, 8))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 6)
        screen.blit(text, textRect)


class ChooseScene:
    def __init__(self, title, *texts):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("UI/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.rects = []
        self.texts = texts
        self.title = title

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 1

        for text in self.texts:
            font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, (HEIGHT // 8 + HEIGHT // 5 * n))
            rect = pygame.Rect((WIDTH - WIDTH_BOX) // 2, textRect.top, WIDTH_BOX, HEIGHT_BOX)
            self.rects.append(rect)
            n += 1
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, pygame.Color(120, 200, 112), rect)
            pygame.draw.rect(screen, pygame.Color(120, 8, 8), rect, 5)
            screen.blit(text, textRect)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    return ('TITLE')

    def element(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                n = 1
                for rect in self.rects:
                    if rect.collidepoint(event.pos):
                        if (n == 1):
                            return (True, True)
                        if (n == 2):
                            return (True, False)
                        if (n == 3):
                            return (False, False)
                    n += 1


class ChessboardScene:
    def __init__(self, title, gs):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(pygame.Color("beige"))  # Fill background with beige color
        bg = pygame.transform.scale(pygame.image.load("UI/image/bg.png"), (B_WIDTH, B_HEIGHT))
        # self.background.blit(bg, (-1, 0))
        self.background.blit(bg, ((WIDTH - B_WIDTH) // 2 - 64, (HEIGHT - B_HEIGHT) // 2))  # Adjusted position
        self.title = title
        self.gs = gs

    """
    Response for all the graphics within a current game state
    """

    def draw(self, screen):
        # Display the game state on the screen
        font = pygame.font.Font(None, 36)
        text = font.render(self.title, True, (255, 255, 255))
        screen.blit(text, (10, 10))
        board = self.gs.board

        # load images of pieces in the chess board
        pieces = ['W', 'B']
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load("ui/image/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

        # Draw the chessboard
        colors = [pygame.Color("dark green"), pygame.Color("dark green")]
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                color = colors[((r + c) % 2)]
                # pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                pygame.draw.rect(screen, color, pygame.Rect((c * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64,
                                                            (r * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2, SQ_SIZE,
                                                            SQ_SIZE))  # Adjusted position

        # # Draw grid lines
        # for r in range(DIMENSION + 1):  # Horizontal lines
        #     # pygame.draw.line(screen, pygame.Color("black"), (0, r * SQ_SIZE), (B_WIDTH, r * SQ_SIZE))
        #     pygame.draw.line(screen, pygame.Color("black"), ((WIDTH - B_WIDTH) // 2 - 64, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2), ((WIDTH - B_WIDTH) // 2 - 64 + B_WIDTH, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2))  # Adjusted position
        # for c in range(DIMENSION + 1):  # Vertical lines
        #     pygame.draw.line(screen, pygame.Color("black"), (c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64, (HEIGHT - B_HEIGHT) // 2), (c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64, (HEIGHT - B_HEIGHT) // 2 + B_HEIGHT))  # Adjusted position
        #     # pygame.draw.line(screen, pygame.Color("black"), (c * SQ_SIZE, 0), (c * SQ_SIZE, HEIGHT))

        # Draw grid lines
        for r in range(DIMENSION):  # Horizontal lines
            pygame.draw.line(screen, pygame.Color("black"),
                             ((WIDTH - B_WIDTH) // 2 - 64, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2), (
                             (WIDTH - B_WIDTH) // 2 - 64 + B_WIDTH,
                             r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2))  # Adjusted position
            # Add row coordinates
            # row_text = font.render(str(DIMENSION - r), True, pygame.Color("black"))
            row_text = font.render(str(r + 1), True, pygame.Color("black"))
            screen.blit(row_text, ((WIDTH - B_WIDTH) // 2 - 100, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2 + SQ_SIZE // 2))

        for c in range(DIMENSION):  # Vertical lines
            pygame.draw.line(screen, pygame.Color("black"),
                             (c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64, (HEIGHT - B_HEIGHT) // 2), (
                             c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64,
                             (HEIGHT - B_HEIGHT) // 2 + B_HEIGHT))  # Adjusted position
            # Add column coordinates
            col_text = font.render(chr(ord('a') + c), True, pygame.Color("black"))
            screen.blit(col_text, (
            c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64 + SQ_SIZE // 2, (HEIGHT - B_HEIGHT) // 2 + B_HEIGHT))

        # Draw the each piece of the chessboard
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = board[r][c]
                if piece != " ":  # not empty square
                    screen.blit(IMAGES[piece], pygame.Rect((c * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64,
                                                           (r * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2, SQ_SIZE,
                                                           SQ_SIZE))  # Adjusted position
                    # screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def update(self, events):
        pass

    def element(self, events):
        pass


class ChessGUI:
    def __init__(self, gs):
        self.gs = gs
        self.selected_piece = None
        self.valid_moves = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    x, y = pygame.mouse.get_pos()
                    row = (y - (HEIGHT - B_HEIGHT) // 2) // SQ_SIZE
                    col = (x - ((WIDTH - B_WIDTH) // 2) + 64) // SQ_SIZE
                    if 0 <= row < DIMENSION and 0 <= col < DIMENSION:
                        piece = self.gs.board[row][col]
                        if piece == self.gs.current_player:  # If the clicked piece belongs to the current player
                            self.selected_piece = (row, col)
                            self.valid_moves = self.gs.get_valid_moves(row, col)
                            self.highlight_valid_moves()

    def highlight_valid_moves(self):
        # Highlight valid moves on the GUI
        for move in self.valid_moves:
            row, col = move
            pygame.draw.rect(screen, pygame.Color("light green"),
                             pygame.Rect((col * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64,
                                         (row * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2, SQ_SIZE, SQ_SIZE))

    def draw_board(self, screen):
        # Draw the chessboard and pieces on the screen
        # Similar to the ChessboardScene draw method, but adapted to use screen as parameter
        pass

    def run_game(self, screen):
        self.running = True
        while self.running:
            self.handle_events()
            self.draw_board(screen)
            pygame.display.flip()
