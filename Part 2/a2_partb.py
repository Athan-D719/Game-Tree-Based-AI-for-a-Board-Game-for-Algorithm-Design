# Main Author: Seyed Iman Modarres Sadeghi
# Main Reviewer: Jonathan Diaz

from a1_partc import Queue
from a1_partd import overflow

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


# this function is your evaluation function for the board
# given a board this function returns the score of the board for the given player in the arguments
def evaluate_board (board, player):
    noOfRows = len(board)
    noOfCols = len(board[0])

    if(isWinning(board, player)):
        return noOfRows * noOfCols * 4
    elif(isWinning(board, player * -1)):
        return noOfRows * noOfCols * -4

    # copiedBoard = copy_board(board)
    # overflow(copiedBoard, Queue())
    score = 0

    for list in board:
        for element in list:
            score += element if player == 1 else element * -1

    return score

# given a board and a player this function returns true if the given player is winning and false otherwise
def isWinning(board, player):
    noOfRows = len(board)
    noOfCols = len(board[0])

    temp = board[0][0]
    for i in range(noOfRows):
        for j in range(noOfCols):
            if(board[i][j] * temp < 0 or temp * player < 0):
                return False
            elif(board[i][j] != 0):
                temp = board[i][j]

    return True		

class GameTree:
    class Node:
        # constructor for the Node class
        def __init__(self, board, depth, player, tree_height = 4):
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []

    # constructor for the GameTree class, this function also makes the tree for the object
    def __init__(self, board, player, tree_height = 4):
        # given a node and a player this function will create the tree to the tree_height that is passed in the constructor's arguments
        def calcChildren(node, player):
            if(node.depth == tree_height - 1 or isWinning(node.board, 1) or isWinning(node.board, -1)):
                node.score = evaluate_board(node.board, node.player)

                return
            
            for row in range(len(node.board)):
                for col in range(len(node.board[0])):
                    if(player * node.board[row][col] >= 0):
                        temp = copy_board(node.board)
                        temp[row][col] += player
                        overflow(temp, Queue())
                        child = self.Node(temp, node.depth + 1, player, tree_height)
                        child.row = row
                        child.col = col
                        node.children.append(child)
                        calcChildren(child, player * -1)

                        minimax = evaluate_board(node.children[0].board, node.player)
                        for childNode in node.children:
                            score = evaluate_board(childNode.board, node.player)
                            if(score > minimax and node.depth % 2 == 0):
                                minimax = score
                            elif(score < minimax and node.depth % 2 == 1):
                                minimax = score

                        node.score = minimax

            

        self.board = board
        self.root = self.Node(board, 0, player, tree_height)
        self.player = player
        self.tree_height = tree_height

        calcChildren(self.root, player)
           

            

        # you will need to implement the creation of the game tree here.  After this function completes,
        # a full game tree will be created.
        # hint: as with many tree structures, you will need to define a self.root that points to the root
        # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
        # need to apply the minimax algorithm to its creation.




    # this function is a pure stub.  It is here to ensure the game runs.  Once you complete
    # the GameTree, you will use it to determine what to return.
    # this function will return the next best move based on the GameTree
    def get_move(self):
        if(not self.root.children):
            return (0, 0)

        rowCol = (self.root.children[0].row, self.root.children[0].col)
        score = self.root.children[0].score
        for childNode in self.root.children:
            if(isWinning(childNode.board, self.player)):
                return (childNode.row, childNode.col)
            if(childNode.score > score):
                rowCol = (childNode.row, childNode.col)
                score = childNode.score

        return rowCol
   
    # this function destroys the game tree   
    def clear_tree(self):
        self.root = None
        self.board = None     
