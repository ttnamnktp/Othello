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
        bg = pygame.transform.scale(pygame.image.load("ui/image/bg.png"), (WIDTH, HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.text = text

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', 80)
        text = font.render(self.text, True, pygame.Color(144, 8, 8))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 3)
        screen.blit(text, textRect)
        play = pygame.transform.scale(pygame.image.load("ui/image/start.png"), (
            pygame.image.load("UI/image/start.png").get_width() // 6,
            pygame.image.load("UI/image/start.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (WIDTH // 2, HEIGHT // 1.5)
        screen.blit(play, self.playRect)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    return ('CHOOSE_MODE')

    def element(self, events):
        pass
