#!/usr/bin/python3

"""! Game class"""
class Game:
    def __init__(self):
        """! Initialize the game"""
        
        self.board = []

    def initBoard(self, size):
        """! Initialize the game board
        @param size Size of the board
        """
        self.board = [[' ' for x in range(size)] for y in range(size)]

    def fillBoard(self, x, y, player):
        """! Fill the game board
        @param x X coordinate
        @param y Y coordinate
        @param player The player character (1 or 2)
        """
        self.board[x][y] = player

    def printBoard(self):
        """! Print the game board"""
        
        print(self.board)

    def getBoardSize(self):
        """! Get the size of the board"""
        
        return (len(self.board))

    def check_valid_case(game, x, y) -> bool:
        """! Check if the case is valid
        @param game The game class
        @param x X coordinate
        @param y Y coordinate
        """
        
        if (game.board[x][y] != ' ' or game.board[x][y] != ' '):
            print("Case already taken", flush=True)
            return False
        return True
