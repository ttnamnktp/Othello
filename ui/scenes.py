import pygame

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


class Button:
    def __init__(self, image_path, scale_factor, position):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            image,
            (image.get_width() // scale_factor, image.get_height() // scale_factor)
        )
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


class SimpleScene:
    def __init__(self, text):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.text = text

        self.play_button = Button("ui/image/start.png", 6, (WIDTH // 2, HEIGHT // 2))
        self.help_button = Button("ui/image/help.png", 9, (WIDTH // 2, HEIGHT // 1.25))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 80)
        text = font.render(self.text, True, pygame.Color(144, 8, 8))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 5)
        screen.blit(text, textRect)

        self.play_button.draw(screen)
        self.help_button.draw(screen)

    def update(self, events):
        for event in events:
            if self.play_button.is_clicked(event):
                return 'CHOOSE_MODE'
            elif self.help_button.is_clicked(event):
                return 'HELP'
        return None


class HelpScene:
    def __init__(self, title, *texts):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.texts = texts
        self.title = title
        self.back_button = Button("ui/image/back.png", 9, (WIDTH // 2, HEIGHT // 1.25))


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

        self.back_button.draw(screen)
    
    def update(self, events):
        for event in events:
            if self.back_button.is_clicked(event):
                return 'TITLE'
        return None


class ChooseScene:
    def __init__(self, title, *texts):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.rects = []
        self.texts = texts
        self.title = title
        self.back_button = Button("ui/image/back.png", 9, (WIDTH // 2, HEIGHT // 1.25))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 1

        for text in self.texts:
            font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, (HEIGHT // 8 + HEIGHT // 5 * n - 10))
            rect = pygame.Rect((WIDTH - WIDTH_BOX) // 2, textRect.top, WIDTH_BOX, HEIGHT_BOX)
            self.rects.append(rect)
            n += 1
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, pygame.Color(120, 200, 112), rect)
            pygame.draw.rect(screen, pygame.Color(120, 8, 8), rect, 5)
            screen.blit(text, textRect)

        self.back_button.draw(screen)


    def update(self, events):
        for event in events:
            if self.play_button.is_clicked(event):
                return 'CHOOSE_MODE'
            elif self.help_button.is_clicked(event):
                return 'HELP'
        return None
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:  # Human vs Human
                            return 'HUMAN_VS_HUMAN'
                        elif i == 1:  # Human vs Bot
                            return 'HUMAN_VS_BOT'         
                if self.back_button.is_clicked(event):
                    return 'TITLE'
        return None


class ChooseBot(ChooseScene):
    def __init__(self, title, *texts):
        super().__init__(title, *texts)
        self.back_button = Button("ui/image/back.png", 9, (WIDTH // 2, HEIGHT // 1.1))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 1

        for text in self.texts:
            font = pygame.font.Font('ui/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text_surface = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text_surface.get_rect()
            textRect.center = (WIDTH // 2, (HEIGHT // 8 + HEIGHT // 5 * n -20))
            rect = pygame.Rect((WIDTH - WIDTH_BOX) // 2, textRect.top, WIDTH_BOX, HEIGHT_BOX)
            self.rects.append(rect)
            n += 1
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, pygame.Color(120, 200, 112), rect)
            pygame.draw.rect(screen, pygame.Color(120, 8, 8), rect, 5)
            # Center the text vertically within the rectangle box
            textRect.centery = rect.centery
            screen.blit(text_surface, textRect)

        self.back_button.draw(screen)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:  # Human vs Human
                            return 'EASY'
                        elif i == 1:  # Human vs Bot
                            return 'MEDIUM' 
                        elif i == 2:  # Bot vs Bot
                            return 'HARD'
                if self.back_button.is_clicked(event):
                    return 'CHOOSE_MODE'
        return None


class ChessboardScene:
    def __init__(self, title, gs):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        # self.background.fill(pygame.Color("beige"))  # Fill background with beige color
        # bg = pygame.transform.scale(pygame.image.load("ui/image/beigebg.png"), (WIDTH, HEIGHT))
        # self.background.blit(bg,(1,1))  # Adjusted position
        self.title = title
        self.gs = gs
        

    def draw(self, screen):
        # Display the game state on the screen
        screen.fill((224, 206, 173))
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg,(0,0))  # Adjusted position
        font = pygame.font.Font(None, 36)
        text = font.render(self.title, True, (255, 255, 255))
        screen.blit(text, (10, 10))
        board = self.gs.board
        
        B_count = self.gs.black_count
        W_count = self.gs.white_count
        turn = self.gs.current_player
        
        text_1 = "Black discs: " + str(int(B_count))
        text_2 = "White discs: " + str(int(W_count))
        text_turn ="Current player: " + str(turn)
        
        text_3 = font.render(text_1,True,(0,0,0))
        text_4 = font.render(text_2,True,(255,255,255))
        text_5 = font.render(text_turn,True, (0,0,0))

        screen.blit(text_3, (630,200))
        screen.blit(text_4, (630,300))
        screen.blit(text_5, (620,400))
        load_images()
        # Draw the chessboard
        colors = [pygame.Color("dark green"), pygame.Color("dark green")]
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                color = colors[((r + c) % 2)]
                pygame.draw.rect(screen, color, pygame.Rect((c * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64,
                                                            (r * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2, SQ_SIZE,
                                                            SQ_SIZE))  # Adjusted position

        # Draw grid lines
        for r in range(DIMENSION + 1):  # Horizontal lines
            pygame.draw.line(screen, pygame.Color("black"),
                             ((WIDTH - B_WIDTH) // 2 - 64, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2), (
                                 (WIDTH - B_WIDTH) // 2 - 64 + B_WIDTH,
                                 r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2))  # Adjusted position
            
        for r in range(DIMENSION):
            # Add row coordinates
            row_text = font.render(str(r + 1), True, pygame.Color("black"))
            screen.blit(row_text, ((WIDTH - B_WIDTH) // 2 - 100, r * SQ_SIZE + (HEIGHT - B_HEIGHT) // 2 + SQ_SIZE // 2))

        for c in range(DIMENSION+1):  # Vertical lines
            pygame.draw.line(screen, pygame.Color("black"),
                             (c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64, (HEIGHT - B_HEIGHT) // 2), (
                                 c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64,
                                 (HEIGHT - B_HEIGHT) // 2 + B_HEIGHT))  # Adjusted position
            
        for c in range(DIMENSION):
            # Add column coordinates
            col_text = font.render(chr(ord('a') + c), True, pygame.Color("black"))
            screen.blit(col_text, (
                c * SQ_SIZE + ((WIDTH - B_WIDTH) // 2) - 64 + SQ_SIZE // 2, (HEIGHT - B_HEIGHT) // 2 + B_HEIGHT + 10))
            

        # Draw each piece of the board
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = board[r][c]
                if piece in IMAGES:  # Ensure the piece is in IMAGES dictionary
                    screen.blit(IMAGES[piece], pygame.Rect((c * SQ_SIZE) + ((WIDTH - B_WIDTH) // 2) - 64,
                                                           (r * SQ_SIZE) + (HEIGHT - B_HEIGHT) // 2, SQ_SIZE,
                                                           SQ_SIZE))  # Adjusted position


class GameOver:
    def __init__(self, game_state):
        self.game_state = game_state
        self.chessboard_scene = ChessboardScene("Othello", game_state)
        self.back_button = Button("ui/image/back.png", 9, (WIDTH // 1.165, HEIGHT // 1.2))

    def draw(self, screen):
        screen.fill((197, 184, 186))
        self.chessboard_scene.draw(screen)
        winner = self.game_state.get_winner()
        font = pygame.font.Font(None, 36)
        winner = self.game_state.get_winner()
        if winner != 'Tie':
            if winner == 'B':
                text = font.render("Game over. Winner: Black ", True, (0, 0, 0))
            if winner == 'W':
                text = font.render("Game over. Winner: White ", True, (255, 255, 255))
        else:
            text = font.render("Game over. It's a Tie!", True, (0, 0, 0))
        self.back_button.draw(screen)
        screen.blit(text, (250,10))
        
    def update(self, events):
        for event in events:
            if self.back_button.is_clicked(event):
                return 'TITLE'
        return None
    
