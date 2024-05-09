from ai.ai import AI
from ai.heuristics.coin_parity import CoinParity
from ai.heuristics.corners_captured import CornersCaptured
from ai.heuristics.static_weight import StaticWeight
from ai.search_algorithms.greedy import Greedy
from ai.search_algorithms.minimax import Minimax
from ai.search_algorithms.minimax_alpha_beta import MinimaxAlphaBeta
from ai.search_algorithms.random import Random
from ai.reinforcement_learning.monte_carlo_search_algorithm import MonteCarloTreeSearch
from engine.GameState import GameState
from engine.Move import Move


def print_state(state):
    for row in state.board:
        print(row)
    print("Current Player:", state.current_player)
    suggest_move(state)


def print_current_move(state, move):
    print(f"{state.current_player}:", move)


def suggest_move(state):
    print(f"Available moves: {Move.get_valid_moves(state)}")


def ai_plays_itself(ai: AI):
    """Test the AI by making it play against itself."""
    state = GameState()
    print()
    print("Initial State")
    while not state.is_game_over():
        print_state(state)
        valid_moves = Move.check_valid_moves_and_set_pass(state)
        if not valid_moves:
            continue
        best_move = ai.return_best_move(state)
        print_current_move(state, best_move)
        state = ai.return_next_state(state, best_move)

    print("Game Over")
    print("Winner:", state.get_winner())


def ai_vs_ai(bot1: AI, bot2: AI):
    """Test the AI by making it play against another AI."""
    state = GameState()
    print()
    # print("Initial State")
    current_player = bot1
    # print("Bot1: Black, Bot2: White")
    while not state.is_game_over():
        # print_state(state)
        valid_moves = Move.check_valid_moves_and_set_pass(state)
        if not valid_moves:
            current_player = bot2 if current_player == bot1 else bot1
            continue
        best_move = current_player.return_best_move(state)
        # if current_player == bot1:
        #     print("Bot1:")
        # else:
        #     print("Bot2:")
        # print_current_move(state, best_move)
        state = current_player.return_next_state(state, best_move)
        current_player = bot2 if current_player == bot1 else bot1

<<<<<<< HEAD
    print("Game Over")
    print("Winner:", state.get_winner())
    return state.black_count, state.white_count
=======
    # print("Game Over")
    # print("Winner:", state.get_winner())

    return state.get_winner()
>>>>>>> 7c2b87af82231c812f32f4fe715f6c3f41b73527


def test_sample():
    # Initialize the AI with the heuristic and search algorithm

    # random_ai = AI(heuristic=None, algorithm=Random, depth=1)
    greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy, depth=3, run_time=1)
    greedy_ai_static_weight = AI(heuristic=StaticWeight(), algorithm=Greedy, depth=3, run_time=1)
    minimax_ai_coin_parity = AI(heuristic=CoinParity(), algorithm=Minimax, depth=3, run_time=1)
    minimax_ai_corners_captured = AI(heuristic=CornersCaptured(), algorithm=Minimax, depth=3, run_time=1)
    minimax_alpha_beta_ai = AI(heuristic=CoinParity(), algorithm=MinimaxAlphaBeta, depth=3, run_time=1)
    minimax_static_weight = AI(heuristic=StaticWeight(), algorithm=Minimax, depth=3, run_time=1)
    minimax_alpha_beta_static_weight = AI(heuristic=StaticWeight(), algorithm=MinimaxAlphaBeta, depth=5, run_time=1)
    # Test the AI by making it play against itself

    random_ai = AI(heuristic=None, algorithm=Random, depth=1)
    greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy, depth=1)
    minimax_ai = AI(heuristic=CoinParity(), algorithm=Minimax, depth=3)
    minimax_alpha_beta_ai = AI(heuristic=CoinParity(), algorithm=MinimaxAlphaBeta, depth=5, run_time=1)
    mcts_ai = AI(heuristic= None, algorithm=MonteCarloTreeSearch, depth=3, run_time=1)

    # ai_plays_itself(ai=random_ai)
    # ai_plays_itself(ai=greedy_ai)
    # ai_plays_itself(ai=minimax_ai)
    # ai_plays_itself(ai=minimax_alpha_beta_ai)
    # ai_plays_itself(ai=minimax_static_weight)

    # Test the AI by making it play against another AI
    # ai_vs_ai(bot1=greedy_ai, bot2=minimax_ai_corners_captured)
    # ai_vs_ai(bot1=random_ai, bot2=greedy_ai)
    # ai_vs_ai(bot1=minimax_ai, bot2=greedy_ai)
    # ai_vs_ai(bot1=minimax_ai, bot2=minimax_alpha_beta_ai)
<<<<<<< HEAD
    return ai_vs_ai(bot1=minimax_alpha_beta_ai, bot2=mcts_ai)
=======

    # ai_vs_ai(bot1=minimax_alpha_beta_ai, bot2=greedy_ai)

    score = {
        'B': 0,
        'W': 0,
        'Tie': 0
    }
    # greedy_ai_static_weight vs greedy_ai
    # for i in range(100):
    #     winner = ai_vs_ai(bot1=greedy_ai_static_weight, bot2=greedy_ai)
    #     score[winner] += 1

    # minimax_alpha_beta_static_weight vs greedy_ai
    for i in range(100):
        winner = ai_vs_ai(bot1=minimax_alpha_beta_static_weight, bot2=greedy_ai)
        score[winner] += 1

    print(score)

    ai_vs_ai(bot1=greedy_ai, bot2=mcts_ai)
>>>>>>> 7c2b87af82231c812f32f4fe715f6c3f41b73527

if __name__ == "__main__":
    test_sample()

