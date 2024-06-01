from ai.ai import AI
from ai.heuristics.coin_parity import CoinParity
from ai.heuristics.dynamic_weight import DynamicWeight
from ai.heuristics.static_weight import StaticWeight
from ai.heuristics.hybrid_heuristic import HybridHeuristic, DynamicHybridHeuristic
from ai.search_algorithms.greedy import Greedy
from ai.search_algorithms.minimax import Minimax
from ai.search_algorithms.minimax_alpha_beta import MinimaxAlphaBeta
from ai.reinforcement_learning.monte_carlo_search_algorithm import MonteCarloTreeSearch
from engine.GameState import GameState
from ui.scenes import *
from ui.ui import *

WIDTH = 832
HEIGHT = 640

B_WIDTH = B_HEIGHT = 512  # board_width and board_height
DIMENSION = 8
SQ_SIZE = B_HEIGHT // DIMENSION  # square_size
MAX_FPS = 15
IMAGES = {}

scenes = {
    'TITLE': SimpleScene('Cờ lật'),
    'CHOOSE_MODE': ChooseScene('Chọn chế độ chơi', 'Người Vs Người', 'Người Vs Máy'),
    'CHOOSE_BOT': ChooseBot('Chọn độ khó', 'EASY', 'MEDIUM', 'HARD'),
    'HELP': HelpScene('Help', 'Othello là một môn thể thao trí tuệ 2 người chơi'),
    'GAME_STATE': ChessboardScene('Othello', GameState()),
    'GAME_OVER': None
}

bots = {
    'EASY': AI(heuristic=CoinParity(), algorithm=Greedy, depth=1),
    'MEDIUM': AI(heuristic=StaticWeight(), algorithm=Minimax, depth=3),
    'HARD': AI(heuristic=StaticWeight(), algorithm=MonteCarloTreeSearch, depth=5)
}


def load_images():
    pieces = ['W', 'B']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("ui/image/" + str(piece).lower() + ".png"),
                                               (SQ_SIZE, SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    load_images()

    gs = GameState()
    running = True
    scene = scenes['TITLE']
    game_over_scene = None
    chess_gui = ChessGUI(gs)

    chess_bot = None
    bot = None
    human_vs_bot_mode = False

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
                    if result != 'TITLE':
                        scene = scenes['HELP']
                    elif result == 'TITLE':
                        scene = scenes['TITLE']
                # Inside the main loop, after handling mouse events in the ChooseScene
                elif scene == scenes['CHOOSE_MODE']:
                    selected_option = scene.update([event])
                    if selected_option:
                        print("ok")
                        if selected_option == 'HUMAN_VS_HUMAN':
                            scene = scenes['GAME_STATE']
                            chess_gui.run_game(screen)  # Run the game in ChessGUI
                            scenes['GAME_OVER'] = GameOver(gs)
                            scene = scenes['GAME_OVER']
                            # Set up the game for Human vs Human
                        elif selected_option == 'HUMAN_VS_BOT':
                            # TODO: Display the ChooseBot scene
                            #  User can choose between 3 difficulties: Easy, Medium, and Hard
                            #  Each difficulty is a different AI.
                            #  There will also be a custom difficulty option where the user can choose
                            #  the algorithm, heuristic and depth of the bot. There will also be a back button to
                            #  return to the ChooseScene
                            scene = scenes['CHOOSE_BOT']
                        elif selected_option == 'TITLE':
                            scene = scenes['TITLE']
                elif scene == scenes['CHOOSE_BOT']:
                    selected_option = scene.update([event])
                    if selected_option == 'CHOOSE_MODE':
                        scene = scenes['CHOOSE_MODE']
                    elif selected_option != 'CHOOSE_MODE':
                        bot = bots[selected_option]
                        chess_bot = ChessBot(gs, bot)
                        scene = scenes['GAME_STATE']
                        human_vs_bot_mode = True

        if human_vs_bot_mode and scene == scenes['GAME_STATE']:
            chess_bot.run_game(screen)  # Run the game in ChessBot
            scenes['GAME_OVER'] = GameOver(gs)
            scene = scenes['GAME_OVER']

        screen.fill((0, 0, 0))  # Clear the screen
        scene.draw(screen)

        pygame.display.flip()  # Update the display
        clock.tick(MAX_FPS)

    pygame.quit()  # Quit pygame when the loop ends


if __name__ == "__main__":
    main()
