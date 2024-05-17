import pygame
import time
from ui.ui import *
from engine.GameState import GameState
from ai.ai import AI
from ai.heuristics.coin_parity import CoinParity
from ai.search_algorithms.minimax import Minimax



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
                # Inside the main loop, after handling mouse events in the ChooseScene
                elif scene == scenes['CHOOSE_MODE']:
                    selected_option = scene.update([event])
                    if selected_option:
                        if selected_option == 'HUMAN_VS_HUMAN':
                            scene = scenes['GAME_STATE']
                            chess_gui = ChessGUI(gs)
                            chess_gui.run_game(screen)  # Run the game in ChessGUI
                            scenes['GAME_OVER'] = GameOver(gs)
                            scene = scenes['GAME_OVER']
                            # Set up the game for Human vs Human
                        elif selected_option == 'HUMAN_VS_BOT':
                            scene = scenes['GAME_STATE']
                            human_turn = True  # Set human player's turn                            
                            # ai_player = AI(CoinParity(), Minimax(), depth=1)
                            if human_turn:
                                chess_gui.handle_events()
                                chess_gui.draw_board(screen)
                                chess_gui.highlight_valid_moves(screen)  # Highlight valid moves
                                pygame.display.flip()
                                human_turn = False
                                print(" human_turn = False")

                            else:
                                # Handle AI player's turn
                                # Use AI logic to determine the best move
                                best_move = ai_player.return_best_move(gs)
                                # Make the move and update game state
                                Move.make_move(gs, best_move)
                                # Switch turn back to human player
                                human_turn = True

                            # Set up the game for Human vs Bot
                        elif selected_option == 'BOT_VS_BOT':
                            # Set up the game for Bot vs Bot
                            scene = scenes['GAME_STATE']
                            
                            


        screen.fill((0, 0, 0))  # Clear the screen
        scene.draw(screen)


        pygame.display.flip()  # Update the display
        clock.tick(MAX_FPS)

    
    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()