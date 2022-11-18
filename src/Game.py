#!/usr/bin/python3

class Game:
    def __init__(self):
        self.board = []

    def initBoard(self, size):
        self.board = [[' ' for x in range(size)] for y in range(size)]

    def fillBoard(self, x, y, player):
        self.board[x][y] = player

    def printBoard(self):
        print(self.board)

    def getBoardSize(self):
        return (len(self.board))

    def check_valid_case(game, x, y) -> bool:
        if (game.board[x][y] != ' ' or game.board[x][y] != ' '):
            print("Case already taken", flush=True)
            return False
        return True