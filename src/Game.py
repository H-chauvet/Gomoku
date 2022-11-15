#!/usr/bin/python3

class Game:
    def __init__(self):
        self.board = None

    def initBoard(self, size):
        self.board = [[' ' for x in range(size)] for y in range(size)]

    def printBoard(self):
        print(self.board)