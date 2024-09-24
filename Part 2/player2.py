from a2_partb import GameTree

class PlayerTwo:

    def __init__(self, name = "P2 Bot", difficulty = 0):
        self.name = name
        self.difficulty = difficulty
        
    def get_name(self):
        return self.name
    
    def set_difficulty(self, difficulty):
        # Difficulties are 0 = Easy, 1 = Medium, 2 = Hard
        self.difficulty = difficulty

    def get_play(self, board):
        tree_height = 0

        # Set tree height to its corresponding difficulty
        match self.difficulty:
            case 0:
                tree_height = 2
            case 1:
                tree_height = 3
            case 2:
                tree_height = 4
            case _:
                tree_height = 2

        tree = GameTree(board, -1, tree_height)
        (row,col) = tree.get_move()
        return (row,col)