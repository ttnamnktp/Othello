import pygame

WIDTH = 640
HEIGHT = 480
HEIGHT_BOX = 50
WIDTH_BOX = 400
NUMBER_DEPTH = 4
WIDTH_PER_BOX = WIDTH_BOX // NUMBER_DEPTH

class SimpleScene:
    def __init__(self, text):
        self.background = pygame.Surface((WIDTH, HEIGHT))
        bg = pygame.transform.scale(pygame.image.load("UI/image/bg.png"), (WIDTH, HEIGHT))
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
        play = pygame.transform.scale(pygame.image.load("UI/image/start.png"), (
            pygame.image.load("UI/image/start.png").get_width() // 6,
            pygame.image.load("UI/image/start.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(play, self.playRect)
        
        help = pygame.transform.scale(pygame.image.load("UI/image/help.png"), (
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
        bg = pygame.transform.scale(pygame.image.load("UI/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.texts = texts
        self.title = title

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 1

        for text in self.texts:
            font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, (HEIGHT // 8 + HEIGHT // 5 * n))
            screen.blit(text, textRect)
            n += 1

        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 40)
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
            font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 35)
            text = font.render(text, True, pygame.Color(144, 8, 8))
            textRect = text.get_rect()
            textRect.center = (640 // 2, (HEIGHT // 8 + HEIGHT // 5 * n))
            rect = pygame.Rect((WIDTH - WIDTH_BOX) // 2, textRect.top, WIDTH_BOX, HEIGHT_BOX)
            self.rects.append(rect)
            n += 1
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, pygame.Color(120, 200, 112), rect)
            pygame.draw.rect(screen, pygame.Color(120, 8, 8), rect, 5)
            screen.blit(text, textRect)

            # font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 40)
            # text = font.render(self.title, True, pygame.Color(144, 8, 8))
            # textRect = text.get_rect()
            # textRect.center = (WIDTH // 2, HEIGHT // 6)
            # screen.blit(text, textRect)
            # play = pygame.transform.scale(pygame.image.load("UI/image/back.png"), (
            #     pygame.image.load("UI/image/back.png").get_width() // 6,
            #     pygame.image.load("UI/image/back.png").get_height() // 6))
            # self.playRect = play.get_rect()
            # self.playRect.center = (WIDTH // 2, HEIGHT // 1.12)
            # screen.blit(play, self.playRect)

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
    def __init__(self, title, game_state):
        self.title = title
        self.game_state = game_state

    def draw(self, screen):
        # Display the game state on the screen
        font = pygame.font.Font(None, 36)
        text = font.render(self.title, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # Draw the chessboard
        for row in range(self.game_state.size):
            for col in range(self.game_state.size):
                pygame.draw.rect(screen, (255, 255, 255), (col * 50, row * 50, 50, 50), 1)

    def update(self, events):
        pass

    def element(self, events):
        pass