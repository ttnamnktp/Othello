import pandas as pd

from ai.ai import AI
from ai.heuristics.coin_parity import CoinParity
from ai.heuristics.static_weight import StaticWeight
from ai.heuristics.hybrid_heuristic import HybridHeuristic
from ai.heuristics.hybrid_heuristic import DynamicHybridHeuristic
from ai.heuristics.dynamic_weight import DynamicWeight

from ai.search_algorithms.greedy import Greedy
from ai.search_algorithms.minimax import Minimax
from ai.search_algorithms.minimax_alpha_beta import MinimaxAlphaBeta
from ai.search_algorithms.random import Random
from ai.reinforcement_learning.monte_carlo_search_algorithm import MonteCarloTreeSearch
from engine.GameState import GameState
from engine.Move import Move

class Statistic():

    MAX_ITERATION = 100

    def __init__(self, bot1, bot2, filename):
        self.bot1 = bot1
        self.bot2 = bot2
        self.filename = filename + '.xlsx'
        self.statistics = {
            'Black Count':[],
            'White Count':[],
            'Difference':[],
            'State':[] # 1 if black win, 0 if tie, -1 if black lose
        }
        self.get_statistics()
        self.export_excel()

    def ai_vs_ai(self):
        """Test the AI by making it play against another AI."""
        bot1 = self.bot1
        bot2 = self.bot2
        state = GameState()
        current_player = bot1
        while not state.is_game_over():
            valid_moves = Move.check_valid_moves_and_set_pass(state)
            if not valid_moves:
                current_player = bot2 if current_player == bot1 else bot1
                continue
            best_move = current_player.return_best_move(state)

            state = current_player.return_next_state(state, best_move)
            current_player = bot2 if current_player == bot1 else bot1

        return state.black_count, state.white_count, state.black_count - state.white_count

    def get_statistics(self):
        for i in range(0, self.MAX_ITERATION):
            print(i)
            black_count, white_count, difference = self.ai_vs_ai()
            state = 1
            if difference == 0:
                state = 0
            elif difference < 0:
                state = -1
            self.statistics['Black Count'].append(black_count)
            self.statistics['White Count'].append(white_count)
            self.statistics['Difference'].append(difference)
            self.statistics['State'].append(state)
        # print(self.statistics)

    def export_excel(self):
        df = pd.DataFrame(self.statistics)
        df.to_excel(self.filename, index=False)

# def check():
#
#     random_ai = AI(heuristic=None, algorithm=Random, depth=1)
#     greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy, depth=1)
#     minimax_ai = AI(heuristic=CoinParity(), algorithm=Minimax, depth=3)
#     minimax_alpha_beta_ai = AI(heuristic=CoinParity(), algorithm=MinimaxAlphaBeta, depth=5, run_time=1)
#     mcts_ai = AI(heuristic= CoinParity(), algorithm=MonteCarloTreeSearch, depth=3, run_time=1)
#
#     minimax_ai = AI(heuristic=DynamicWeight(), algorithm=Minimax, depth=3)
#     minimax_alpha_beta_ai = AI(heuristic=DynamicWeight(), algorithm=MinimaxAlphaBeta, depth=5, run_time=1)
#     mcts_ai = AI(heuristic=StaticWeight(), algorithm=MonteCarloTreeSearch, depth=3, run_time=1)
#     minimax_alpha_beta_ai_dynamic = AI(heuristic=DynamicWeight(), algorithm=MinimaxAlphaBeta, depth=4, run_time=1)
#     minimax_alpha_beta_ai_static = AI(heuristic=StaticWeight(), algorithm=MinimaxAlphaBeta, depth=4, run_time=1)
#     minimax_alpha_beta_ai_hybrid = AI(heuristic=HybridHeuristic(), algorithm=MinimaxAlphaBeta, depth=4, run_time=1)
#     minimax_alpha_beta_ai_dynamic_hybrid = AI(heuristic=DynamicHybridHeuristic(), algorithm=MinimaxAlphaBeta, depth=4, run_time=1)
#
#     return Statistic.ai_vs_ai(bot1=random_ai, bot2=random_ai)


# random_ai = AI(heuristic=None, algorithm=Random, depth=1)
# greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy, depth=1)
# st = Statistic(random_ai,greedy_ai,"example")

