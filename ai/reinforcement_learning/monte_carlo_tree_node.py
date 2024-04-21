class Node():

    def __init__(self, game_state, move, parent_node):
        # init associated game state
        self.game_state = game_state
        self.is_terminal = False
        self.move = move

        # check if it is a terminal node
        if self.game_state.is_game_over():
            self.is_terminal = True

        # init is fully expanded flag
        self.is_fully_expanded = self.is_terminal

        # init parent node if available
        self.parent_node = parent_node

        # init the number of node visits
        self.visits = 0

        # init the total score of the node
        self.score = 0

        # init current node's children
        self.children_node = {}


