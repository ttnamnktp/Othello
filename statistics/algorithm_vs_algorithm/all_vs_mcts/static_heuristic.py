import statistics.statistic
from statistics.statistic import Statistic


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

random_ai = AI(heuristic=None, algorithm=Random, depth=1)
greedy_ai = AI(heuristic=CoinParity(), algorithm=Greedy, depth=1)
minimax_ai = AI(heuristic=CoinParity(), algorithm=Minimax, depth=3)
minimax_alpha_beta_ai = AI(heuristic=CoinParity(), algorithm=MinimaxAlphaBeta, depth=5, run_time=1)
mcts_ai = AI(heuristic= CoinParity(), algorithm=MonteCarloTreeSearch, depth=3, run_time=1)

st1 = Statistic(random_ai,mcts_ai,"example1")
st2 = Statistic(greedy_ai,mcts_ai,"example2")
st3 = Statistic(minimax_ai,mcts_ai,"example3")
st4 = Statistic(minimax_alpha_beta_ai,mcts_ai,"example4")
