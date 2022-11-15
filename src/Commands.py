#!/usr/bin/python3

from src.Game import Game

class Commands:

    def __init__(self):
        self.commands = {
            'start': self.start,
            'turn': self.turn,
            'begin': self.begin,
            'board': self.board,
            'info': self.info,
            'about': self.about,
        }

    def start(self, game: Game):
        game.initBoard(20)
        print('OK - everything is good', flush=True)

    def turn(self, game: Game):
        game.fillBoard(10, 10, 2)
        game.fillBoard(11, 10, 1)
        print('11,10', flush=True)

    def begin(self, game: Game):
        print('10,10', flush=True)

    def board(self, game: Game):
        print('board', flush=True)

    def info(self, game: Game):
        print('info', flush=True)

    def about(self, game: Game):
        print('about', flush=True)

    def executeCommand(self, command, game: Game, params):
        try:
            self.commands[command](game)
        except:
            return