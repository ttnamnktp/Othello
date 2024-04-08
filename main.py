import pygame
import time
from ui.ui import *
from engine.GameState import GameState

WIDTH = 832
HEIGHT = 832
C_DIMENSION = 9
R_DIMENSION = 11
SQ_SIZE = 64
MAX_FPS = 10
IMAGES = {}

scenes = {
    'TITLE': SimpleScene('Cờ toán Việt Nam'),
    'CHOOSE_MODE': ChooseScene('Chọn chế độ chơi', 'Người Vs Người', 'Người Vs Máy', 'Máy Vs Máy'),
    # 'CHOOSE_BOT': ChooseBot('Chọn Bot', 'Negamax', 'Negascout', 'Minimax', 'Greedy'),
    'HELP': HelpScene('Help', 'Your help text here.'),
    'GAME_STATE': ChessboardScene('Game State', GameState())
}

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    # gs = GameState()
    end_UI = True
    scene = scenes['TITLE']    

    running = True
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
                elif scene == scenes['CHOOSE_MODE']:
                    selected_option = scene.element([event])
                    if selected_option:
                        if selected_option == (True, True):
                            scene = scenes['GAME_STATE']
                    # # If currently in the ChooseBot scene
                    # selected_bot = scene.element([event])  # Get the selected bot option
                    # if selected_bot:  # If a bot option is selected
                    #     # Switch to the corresponding game mode based on the selected bot
                    #     if selected_bot == 'Negamax':
                    #         # Initialize the game with Negamax AI bot
                    #         # Replace this with your game initialization code
                    #         pass
                    #     elif selected_bot == 'Negascout':
                    #         # Initialize the game with Negascout AI bot
                    #         # Replace this with your game initialization code
                    #         pass
                    #     elif selected_bot == 'Minimax':
                    #         # Initialize the game with Minimax AI bot
                    #         # Replace this with your game initialization code
                    #         pass
                    #     elif selected_bot == 'Greedy':
                    #         # Initialize the game with Greedy AI bot
                    #         # Replace this with your game initialization code
                    #         pass
                    #     # After initializing the game mode, switch to the game scene
                    #     # Replace 'GAME' with your actual game scene
                    #     # scene = scenes['GAME']
                    #     scene = scenes['TITLE']


        scene.draw(screen)  # Draw the scene on the screen
        pygame.display.flip()  # Update the display
        clock.tick(MAX_FPS)  # Limit the frame rate to MAX_FPS frames per second

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()