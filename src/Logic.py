#!/usr/bin/python3

import random
from src.Game import Game 

class Logic:

    def __init__(self):
        self.x = 0
        self.y = 0

    def getBestMove(self, game: Game):
        while True:
            self.x = random.randint(0, game.getBoardSize() - 1)
            self.y = random.randint(0, game.getBoardSize() - 1)
            if (game.board[self.y][self.x] == ' '):
                break
        return ((self.x, self.y))