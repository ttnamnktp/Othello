import pygame
import time
from ui.ui import *
from engine.GameState import GameState

WIDTH = 832
HEIGHT = 640

B_WIDTH = B_HEIGHT = 512  # board_width and board_height
DIMENSION = 8
SQ_SIZE = B_HEIGHT // DIMENSION  # square_size
MAX_FPS = 15
IMAGES = {}

scenes = {
    'TITLE': SimpleScene('Cờ lật'),
    'CHOOSE_MODE': ChooseScene('Chọn chế độ chơi', 'Người Vs Người', 'Người Vs Máy', 'Máy Vs Máy'),
    # 'CHOOSE_BOT': ChooseBot('Chọn Bot', 'Negamax', 'Negascout', 'Minimax', 'Greedy'),
    'HELP': HelpScene('Help', 'Your help text here.'),
    'GAME_STATE': ChessboardScene('Cờ lật', GameState()),
    'GAME_OVER': None
}


def load_images():
    pieces = ['W', 'B']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("ui/image/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    load_images()

    gs = GameState()
    running = True
    scene = scenes['TITLE']
    chess_gui = ChessGUI(gs)
    game_over_scene = None

    while running:  # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop and close the program if the user closes the window
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks
                if scene == scenes['TITLE']:
                    result = scene.update([event])  # Pass the event to the scene's update method
                    if result == 'CHOOSE_MODE':
                        scene = scenes['CHOOSE_MODE']
                    elif result == 'HELP':
                        scene = scenes['HELP']
                elif result == 'HELP':
                    result = scene.update([event])
                    if result == 'TITLE':
                        scene = scenes['TITLE']
                elif scene == scenes['CHOOSE_MODE']:
                    selected_option = scene.element([event])
                    if selected_option:
                        scene = scenes['GAME_STATE']
                        chess_gui.run_game(screen)  # Run the game in ChessGUI
                        scenes['GAME_OVER'] = GameOver(gs)
                        scene = scenes['GAME_OVER']


        screen.fill((0, 0, 0))  # Clear the screen
        scene.draw(screen)


        pygame.display.flip()  # Update the display
        clock.tick(MAX_FPS)

    
    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()