#!/usr/bin/python3

class Game:
    def __init__(self):
        self.board = None

    def initBoard(self, size):
        self.board = [[' ' for x in range(size)] for y in range(size)]

    def fillBoard(self, x, y, player):
        self.board[y][x] = player

    def printBoard(self):
        print(self.board)

    def getBoardSize(self):
        return (len(self.board))