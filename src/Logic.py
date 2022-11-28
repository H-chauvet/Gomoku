#!/usr/bin/python3

import random
from src.Game import Game 

class Logic:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.whichPattern = 0
        self.suite = 0
        self.numberToFind = 0

    def fillCaseFour(self, game: Game, x: int, y: int) -> bool:
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

    def fillCaseThree(self, game: Game, x, y) -> bool:
        if (self.whichPattern == 1):
            # Line
            if (game.board[x][y - 3] == '2' and game.board[x][y - 2] == '2' and game.board[x][y - 1] == '2'):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True                    
                elif game.board[x][y - 4] == ' ':
                    self.x = x
                    self.y = y - 4
                    return True
            elif game.board[x][y - 4] == '2' and game.board[x][y - 3] == '2' and game.board[x][y - 2] == '2':
                if game.board[x][y - 1] == ' ':
                    self.x = x
                    self.y = y - 1
                    return True
            elif game.board[x][y - 2] == '2' and game.board[x][y - 1] == '2' and game.board[x][y] == '2':
                if game.board[x][y - 3] == ' ':
                    self.x = x
                    self.y = y - 3
                    return True
            elif (game.board[x][y - 4] == '2' and game.board[x][y - 3] == '2' and game.board[x][y - 2] == ' ' and game.board[x][y - 1] == '2' and game.board[x][y] == ' ') or (game.board[x][y - 4] == ' ' and game.board[x][y - 3] == '2' and game.board[x][y - 2] == '2' and game.board[x][y - 1] == ' ' and game.board[x][y] == '2') or (game.board[x][y - 4] == '2' and game.board[x][y - 3] == ' ' and game.board[x][y - 2] == '2' and game.board[x][y - 1] == '2' and game.board[x][y] == ' ') or (game.board[x][y - 4] == ' ' and game.board[x][y - 3] == '2' and game.board[x][y - 2] == ' ' and game.board[x][y - 1] == '2' and game.board[x][y] == '2'):
                if game.board[x][y - 2] == ' ':
                    self.x = x
                    self.y = y - 2
                    return True
                elif game.board[x][y - 1] == ' ':
                    self.x = x
                    self.y = y - 1
                    return True
                elif game.board[x][y - 3] == ' ':
                    self.x = x
                    self.y = y - 3
                    return True
        if (self.whichPattern == 2):
            # Colomn
            if (game.board[x - 3][y] == '2' and game.board[x - 2][y] == '2' and game.board[x - 1][y] == '2'):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True                    
                elif game.board[x - 4][y] == ' ':
                    self.x = x - 4
                    self.y = y
                    return True
            elif game.board[x - 4][y] == '2' and game.board[x - 3][y] == '2' and game.board[x - 2][y] == '2':
                if game.board[x - 1][y] == ' ':
                    self.x = x - 1
                    self.y = y
                    return True
            elif game.board[x - 2][y] == '2' and game.board[x - 1][y] == '2' and game.board[x][y] == '2':
                if game.board[x - 3][y] == ' ':
                    self.x = x - 3
                    self.y = y
                    return True
            elif (game.board[x - 4][y] == '2' and game.board[x - 3][y] == '2' and game.board[x - 2][y] == ' ' and game.board[x - 1][y] == '2' and game.board[x][y] == ' ') or (game.board[x - 4][y] == ' ' and game.board[x - 3][y] == '2' and game.board[x - 2][y] == '2' and game.board[x - 1][y] == ' ' and game.board[x][y] == '2') or (game.board[x - 4][y] == '2' and game.board[x - 3][y] == ' ' and game.board[x - 2][y] == '2' and game.board[x - 1][y] == '2' and game.board[x][y] == ' ') or (game.board[x - 4][y] == ' ' and game.board[x - 3][y] == '2' and game.board[x - 2][y] == ' ' and game.board[x - 1][y] == '2' and game.board[x][y] == '2'):
                if game.board[x - 2][y] == ' ':
                    self.x = x - 2
                    self.y = y
                    return True
                elif game.board[x - 1][y] == ' ':
                    self.x = x - 1
                    self.y = y
                    return True
                elif game.board[x - 3][y] == ' ':
                    self.x = x - 3
                    self.y = y
                    return True
        elif self.whichPattern == 3:
            # Diagonal A
            x -= 5
            y -= 4
            if (game.board[x + 1][y + 1] == '2' and game.board[x + 2][y + 2] == '2' and game.board[x + 3][y + 3] == '2'):
                if game.board[x][y] == ' ':
                    self.x = x
                    self.y = y
                    return True                    
                elif game.board[x + 4][y + 4] == ' ':
                    self.x = x + 4
                    self.y = y + 4
                    return True
            elif game.board[x + 4][y + 4] == '2' and game.board[x + 3][y + 3] == '2' and game.board[x + 2][y + 2] == '2':
                if game.board[x + 1][y + 1] == ' ':
                    self.x = x + 1
                    self.y = y + 1
                    return True
            elif game.board[x][y] == '2' and game.board[x + 1][y + 1] == '2' and game.board[x + 2][y + 2] == '2':
                if game.board[x + 3][y + 3] == ' ':
                    self.x = x + 3
                    self.y = y + 3
                    return True
            elif (game.board[x][y] == '2' and game.board[x + 1][y + 1] == '2' and game.board[x + 2][y + 2] == ' ' and game.board[x + 3][y + 3] == '2' and game.board[x + 4][y + 4] == ' ') or (game.board[x][y] == ' ' and game.board[x + 1][y + 1] == '2' and game.board[x + 2][y + 2] == '2' and game.board[x + 3][y + 3] == ' ' and game.board[x + 4][y + 4] == '2') or (game.board[x][y] == '2' and game.board[x + 1][y + 1] == ' ' and game.board[x + 2][y + 2] == '2' and game.board[x + 3][y + 3] == '2' and game.board[x + 4][y + 4] == ' ') or (game.board[x][y] == ' ' and game.board[x + 1][y + 1] == '2' and game.board[x + 2][y + 2] == ' ' and game.board[x + 3][y + 3] == '2' and game.board[x + 4][y + 4] == '2'):
                if game.board[x + 1][y + 1] == ' ':
                    self.x = x + 1
                    self.y = y + 1
                    return True
                elif game.board[x + 2][y + 2] == ' ':
                    self.x = x + 2
                    self.y = y + 2
                    return True
                elif game.board[x + 3][y + 3] == ' ':
                    self.x = x + 3
                    self.y = y + 3
                    return True
        return False

    def fillCase(self, game: Game, x, y) -> bool:
        if self.suite == 4:
            if self.fillCaseFour(game, x, y) == True:
                return True
        elif self.suite == 3:
            if self.fillCaseThree(game, x, y) == True:
                return True
        return False

    def findPattern(self, game: Game, x, y) -> bool:
        counter = 0
        # Line
        for i in range(0, y):
            for j in range(0, x - 4):
                for j in range(j, j + 5):
                    if game.board[i][j] == self.numberToFind:
                        counter += 1
                if (counter == self.suite):
                    self.whichPattern = 1
                    if self.fillCase(game, i, j) == True:
                        return True
                counter = 0
                self.whichPattern = 0

        # Colomn
        for j in range(0, y):
            for i in range(0, x - 4):
                for i in range(i, i + 5):
                    if game.board[i][j] == self.numberToFind:
                        counter += 1
                if (counter == self.suite):
                    self.whichPattern = 2
                    if self.fillCase(game, i, j) == True:
                        return True
                counter = 0
                self.whichPattern = 0

        # Diagonal A
        i = 0
        while (i != x - 4):
            for j in range(0, y - 4):
                for j in range(j, j + 5):
                    if game.board[i][j] == self.numberToFind:
                        counter += 1
                    i += 1
                if (counter == self.suite):
                    self.whichPattern = 3
                    if self.fillCase(game, i, j) == True:
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
                        if game.board[i][j] == self.numberToFind:
                            counter += 1
                        i += 1
                        j -= 1
                        count_j += 1
                    if (counter == self.suite):
                        self.whichPattern = 4
                        if self.fillCase(game, i, j) == True:
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

    def semiDefense(self, game: Game, x, y) -> bool:
        self.suite = 3
        if self.findPattern(game, x, y) == True:
            return True
        return False

    def semiAttack(self, game: Game, x, y) -> bool:
        # si case de chaque coté des 3 aligné en placer sur un des deux
        return False

    def controlledRandom(self, game: Game, x, y):
        for i in range(len(game.board) - 1):
            for j in range(len(game.board[i]) - 1):
                if game.board[i + 1][j] == '1' or game.board[i - 1][j] == '1' or game.board[i][j + 1] == '1' or game.board[i][j - 1] == '1' or game.board[i + 1][j + 1] == '1' or game.board[i - 1][j - 1] == '1' or game.board[i + 1][j - 1] == '1' or game.board[i - 1][j + 1] == '1':
                    if game.board[i][j] == ' ':
                        self.x = i
                        self.y = j
                        return True
        return False
        
    def getBestMove(self, game: Game, x, y):
        self.suite = 4
        self.numberToFind = '1'
        if self.findPattern(game, x, y) == True:
            return ((self.x, self.y))

        self.numberToFind = '2'
        if self.findPattern(game, x, y) == True:
            return ((self.x, self.y))

        self.suite = 3
        if self.semiDefense(game, x, y) == True:
            return ((self.x, self.y))

        self.numberToFind = '1'
        if self.semiAttack(game, x, y) == True:
            return ((self.x, self.y))
        if self.controlledRandom(game, x, y) == True:
            return ((self.x, self.y))
        else:
            self.x = random.randint(0, x - 1)
            self.y = random.randint(0, y - 1)
            while (game.board[self.x][self.y] != ' '):
                self.x = random.randint(0, x - 1)
                self.y = random.randint(0, y - 1)
        return ((self.x, self.y))
