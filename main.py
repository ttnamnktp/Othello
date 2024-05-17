import pygame
import time
from ui.ui import *
from engine.GameState import GameState

WIDTH = 832
# HEIGHT = 512
HEIGHT = 640

# C_DIMENSION = 9
# R_DIMENSION = 11
# SQ_SIZE = 64
# MAX_FPS = 10
# IMAGES = {}
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
    'GAME_STATE': ChessboardScene('Cờ lật', GameState())
}

def load_images():
    pieces = ['W', 'B']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("ui/image/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    load_images()  # load images before the while loop
    gs = GameState()
    end_UI = True
    running = True
    scene = scenes['TITLE']
    chess_gui = ChessGUI(gs)

    # # branch main
    # while running:  # Main game loop
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False  # Exit the loop and close the program if the user closes the window
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             # Handle mouse clicks
    #             if scene == scenes['TITLE']:
    #                 result = scene.update([event])  # Pass the event to the scene's update method
    #                 if result == 'CHOOSE_MODE':
    #                     scene = scenes['CHOOSE_MODE']
    #                 elif result == 'HELP':
    #                     scene = scenes['HELP']
    #             elif scene == scenes['CHOOSE_MODE']:
    #                 selected_option = scene.element([event])
    #                 if selected_option:
    #                     scene = scenes['GAME_STATE']

    #                     # if selected_option == (True, True):
    #                     #     scene = scenes['TITLE']
    #     scene.draw(screen)  # Draw the scene on the screen
    #     pygame.display.flip()  # Update the display
    #     clock.tick(MAX_FPS)  # Limit the frame rate to MAX_FPS frames per second

    # pygame.quit()  # Quit pygame when the loop ends

    # branch feature
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
                        pass  # Handle help scene
                elif scene == scenes['CHOOSE_MODE']:
                    selected_option = scene.element([event])
                    if selected_option:
                        scene = scenes['GAME_STATE']
                        chess_gui.handle_events()  # Pass events to ChessGUI if in game state
                        print("Den day handle event")

                        chess_gui.run_game(screen)  # Run the game in ChessGUI
                        pygame.display.flip()  # Update the display


        screen.fill((0, 0, 0))  # Clear the screen
        scene.draw(screen)  # Draw the current scene
        pygame.display.flip()  # Update the display
        clock.tick(MAX_FPS)


    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()