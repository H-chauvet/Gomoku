#!/usr/bin/python3

"""! Game class"""
class Game:
    def __init__(self):
        """! Initialize the game"""
        
        self.board = []

    def initBoard(self, size: int):
        """! Initialize the game board
        @param size Size of the board
        """
        self.board = [[' ' for x in range(size)] for y in range(size)]

    def fillBoard(self, x: int, y: int, player: str):
        """! Fill the game board
        @param x X coordinate
        @param y Y coordinate
        @param player The player character (1 or 2)
        """
        self.board[x][y] = player

    def printBoard(self):
        """! Print the game board"""
        
        print(self.board)

    def getBoardSize(self) -> int:
        """! Get the size of the board"""
        
        return (len(self.board))
