class Node():

    def __init__(self, game_state, move, parent_node, depth):
        # init associated game state
        self.game_state = game_state
        self.is_terminal = False
        self.move = move
        self.depth = depth

        # check if it is a terminal node
        if self.game_state.is_terminal():
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

    def check_fully_expanded(self):
        states = self.game_state.generate_states()
        # loop over generated states (moves)
        for state in states:
            # make sure that current state (move) is not present in child nodes
            if str(state[0].board) not in self.children_node:
                self.is_fully_expanded = False
                return False
        self.is_fully_expanded = True
        return True


