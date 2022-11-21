#!/usr/bin/python3

import random
from src.Game import Game 

class Logic:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.whichPattern = 0

    def findDefense(self, game: Game, x, y) -> bool:
        if (self.whichPattern == 1):
            for y in range(y - 4, y + 1):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True
        elif self.whichPattern == 2:
            for x in range(x - 4, x + 1):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True
        elif self.whichPattern == 3:
            x -= 5
            y -= 4
            for x in range(x, x + 5):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True
                y += 1
        elif self.whichPattern == 4:
            x -= 5
            y += 5
            for x in range(x, x + 5):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True
                y -= 1
        return False

    def finPatternDeffense(self, game: Game, x, y) -> bool:
        counter = 0
        # Line
        for i in range(0, y):
            for j in range(0, x - 4):
                for j in range(j, j + 5):
                    if game.board[i][j] == '2':
                        counter += 1
                if (counter == 4):
                    self.whichPattern = 1
                    if self.findDefense(game, i, j) == True:
                        return True
                counter = 0
                self.whichPattern = 0

        # Colomn
        for j in range(0, y):
            for i in range(0, x - 4):
                for i in range(i, i + 5):
                    if game.board[i][j] == '2':
                        counter += 1
                if (counter == 4):
                    self.whichPattern = 2
                    if self.findDefense(game, i, j) == True:
                        return True
                counter = 0
                self.whichPattern = 0

        # Diagonal A
        i = 0
        while (i != x - 4):
            for j in range(0, y - 4):
                for j in range(j, j + 5):
                    if game.board[i][j] == '2':
                        counter += 1
                    i += 1
                if (counter == 4):
                    self.whichPattern = 3
                    if self.findDefense(game, i, j) == True:
                        return True
                counter = 0
                self.whichPattern = 0
                i -= 5
            i += 1
            
        # Diagonal B
        i = 0
        j = y - 1
        count_j = 0
        count_i = 0
        while count_i != x - 4:
            while (i != x - 4):
                while j != 4:
                    while count_j != 5:
                        if game.board[i][j] == '2':
                            counter += 1
                        i += 1
                        j -= 1
                        count_j += 1
                    if (counter == 4):
                        self.whichPattern = 4
                        if self.findDefense(game, i, j) == True:
                            return True
                    counter = 0
                    count_j = 0
                    self.whichPattern = 0
                    j += 4
                    i -= 5
                i += 1
                j = y - 1
            count_i += 1
        return False

    def getBestMove(self, game: Game, x, y):
        while True:
            if self.finPatternDeffense(game, x, y) == False:
                self.x = random.randint(0, game.getBoardSize() - 1)
                self.y = random.randint(0, game.getBoardSize() - 1)
                if (game.board[self.y][self.x] == ' '):
                    break
            else:
                break
        return ((self.x, self.y))
