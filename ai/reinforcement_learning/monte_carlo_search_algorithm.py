# import module
from ai.search_algorithms.search_algorithm import SearchAlgorithm
from ai.reinforcement_learning.monte_carlo_tree_node import Node
# import processing library package
import math
import random

from engine.GameState import GameState
from engine.GameState import Move

class MonteCarloTreeSearch(SearchAlgorithm):

    def find_move(self, game_state: GameState(), depth: int) -> (int, int):
        # create root node
        self.root = Node(game_state, None,None)

        # walk through 1000 iterations
        for iteration in range(1000):
            # select a node (selection phase)
            node = self.select(self.root)

            # scrore current node (simulation phase)
            score = self.rollout(node.game_state)

            # backpropagate results
            self.backpropagate(node, score)

        # pick up the best move in the current position
        try:
            return self.get_best_move(self.root, 0)

        except:
            pass

    # select most promising node
    def select(self, node):
        # make sure that we're dealing with non-terminal nodes
        while not node.is_terminal:
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
            # make sure that current state (move) is not present in child nodes
            if str(state[0].board) not in node.children_node:
                # create a new node
                new_node = Node(state[0], state[1], node)

                # add child node to parent's node children_node list (dict)
                node.children_node[str(state[0].board)] = new_node

                # case when node is fully expanded
                if len(states) == len(node.children_node):
                       node.is_fully_expanded = True

                # return newly created node
                return new_node

        # debugging
        print('Should not get here!!!')

    # simulate the game via making random moves until reach end of the game
    def rollout(self, game_state):
        # make random moves for both sides until terminal state of the game is reached
        while not game_state.is_game_over():
            # try to make a move
            try:
                # make the on board
                game_state = random.choice(game_state.generate_states())[0]

            # no moves available
            except:
                # return a draw score
                return 0

        # return score from the player "W" perspective
        if game_state.current_player == 'W':
            return 1
        elif game_state.current_player == 'B':
            return -1

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):
        # update nodes's up to root node
        while node is not None:
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
            # define current player
            if child_node.game_state.current_player == 'W':
                current_player = 1
            elif child_node.game_state.current_player == 'B':
                current_player = -1

            # get move score using UCT formula
            move_score = current_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(
                math.log(node.visits / child_node.visits))

            # better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)

        # return one of the best moves randomly
        return random.choice(best_moves).move