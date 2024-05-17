# import module
from ai.search_algorithms.search_algorithm import SearchAlgorithm
from ai.reinforcement_learning.monte_carlo_tree_node import Node
from engine.GameState import GameState
from engine.GameState import Move

# import processing library package
import math
import random

DEPTH = 15

weight_matrix = [
    [400, -80, 76, 44, 44, 76, -80, 400],
    [-80, -350, -10, -10, -10, -10, -350, -80],
    [16, -10, 20, 0, 0, 20, -10, 16],
    [4, -10, 0, 1, 1, 0, -10, 4],
    [4, -10, 0, 1, 1, 0, -10, 4],
    [16, -10, 20, 0, 0, 20, -10, 16],
    [-80, -350, -10, -10, -10, -10, -350, -80],
    [400, -80, 76, 44, 44, 76, -80, 400]
]
class MonteCarloTreeSearch(SearchAlgorithm):

    def find_move(self, game_state: GameState(), depth: int) -> (int, int):
        result = self.search(game_state, depth)
        if isinstance(result, Node):
            return result.move
        return result

    def search(self, game_state: GameState(), depth) -> (int, int):
        # create root node
        self.root = Node(game_state, None,None, 0)

        # walk through 1000 iterations
        for iteration in range(100):
            print(0)
            # select a node (selection phase)
            node = self.select(self.root)

            # scrore current node (simulation phase)
            score = self.simulation(node.game_state)

            # backpropagate results
            self.backpropagate(node, score)

        # pick up the best move in the current position
        try:
            return self.get_best_move(self.root, 0)

        except:
            valid_moves = Move.get_valid_moves(game_state)
            return random.choice(valid_moves)

    # select most promising node
    def select(self, node):
        # make sure that we're dealing with non-terminal nodes

        while (not node.is_terminal) and node.depth < DEPTH:
            print(1)
            # case where the node is fully expanded
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)

            # case where the node is not fully expanded
            else:
                # otherwise expand the node
                return self.expand(node)

        # return node
        return node

    # expand node
    def expand(self, node):
        # generate legal states (moves) for the given node
        states = node.game_state.generate_states()

        # loop over generated states (moves)
        for state in states:
            print(2)
            # make sure that current state (move) is not present in child nodes
            if str(state[0].board) not in node.children_node:
                # create a new node
                new_node = Node(state[0], state[1], node, node.depth + 1)

                # add child node to parent's node children_node list (dict)
                node.children_node[str(state[0].board)] = new_node

                # case when node is fully expanded
                if len(states) == len(node.children_node):
                       node.is_fully_expanded = True

                # return newly created node
                return new_node

        # debugging
        # print('Should not get here!!!')

    # simulate the game via making random moves until reach end of the game
    def simulation(self, game_state):
        # make random moves for both sides until terminal state of the game is reached
        depth_it = 0
        while not game_state.is_game_over() and depth_it < int(DEPTH/4):
        # while not game_state.is_game_over():

            depth_it = depth_it + 1
            print(3)
            # try to make a move
            try:
                # make the on board
                game_state = random.choice(game_state.generate_states())[0]

            # no moves available
            except:
                # return a game_state score
                return self.heuristic.evaluate(game_state)

        # return score from the player "W" perspective
        return self.heuristic.evaluate(game_state)

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):
        # update nodes's up to root node
        while node is not None:
            # print(4)
            # update node's visits
            node.visits += 1

            # update node's score
            node.score += score

            # set node to parent
            node = node.parent_node

    # select the best node basing on UCB1 formula
    def get_best_move(self, node, exploration_constant):
        # define best score & best moves
        best_score = float('-inf')
        best_moves = []

        # loop over child nodes
        for child_node in node.children_node.values():
            # print(5)
            # define current player
            # current_player = 1
            #
            # if child_node.game_state.current_player == 'B':
            #     current_player = -1

            # get move score using UCT formula
            move_score = 0.1 * child_node.score / child_node.visits + exploration_constant * math.sqrt(
                math.log(node.visits / child_node.visits))

            # better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)

        # return one of the best moves randomly
        return random.choice(best_moves)

    # def evaluate(self, game_state: GameState()) -> int:
    #     score = 0
    #     current_player = 1
    #     if game_state.current_player == 'B':
    #         current_player = -1
    #     for i in range(8):
    #         for j in range(8):
    #             k = 0
    #             if game_state.board[i][j] == 'W':
    #                 k = 1
    #             elif game_state.board[i][j] == 'B':
    #                 k = -1
    #             score += weight_matrix[i][j] * k
    #     # return score +  100 * (game_state.white_count - game_state.black_count) / (game_state.white_count + game_state.black_count)
    #     return (score + (game_state.white_count - game_state.black_count)) * current_player