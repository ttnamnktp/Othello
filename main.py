from ui.ui import *

WIDTH = 832
HEIGHT = 832
C_DIMENSION = 9
R_DIMENSION = 11
SQ_SIZE = 64
MAX_FPS = 10
IMAGES = {}

scenes = {
    'TITLE': SimpleScene('Cờ toán Việt Nam'),
}

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    # clock = pygame.time.Clock()
    # gs = GameState()
    scene = scenes['TITLE']


    scene.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
    main()