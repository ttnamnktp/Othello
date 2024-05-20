import pygame
from engine.GameState import GameState as gs
from engine.Move import Move

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
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 80)
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
                for i, rect in enumerate(self.rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:  # Human vs Human
                            return 'HUMAN_VS_HUMAN'
                        elif i == 1:  # Human vs Bot
                            return 'HUMAN_VS_BOT'
                        elif i == 2:  # Bot vs Bot
                            return 'BOT_VS_BOT'
        return None

class ChooseBot (ChooseScene):
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:  # Human vs Human
                            return 'BOT 1'
                        elif i == 1:  # Human vs Bot
                            return 'BOT 2'
                        elif i == 2:  # Bot vs Bot
                            return 'BOT 3'
                        else:
                            return 'BOT 4'

        return None
    
