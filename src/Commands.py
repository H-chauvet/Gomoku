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
            'end': self.end,
            'about': self.about,
        }

    def start(self, game: Game):
        game.initBoard(20)
        print('start', flush=True)

    def turn(self, game: Game):
        print('turn', flush=True)

    def begin(self, game: Game):
        print('begin', flush=True)

    def board(self, game: Game):
        print('board', flush=True)

    def info(self, game: Game):
        print('info', flush=True)

    def end(self, game: Game):
        print('end', flush=True)

    def about(self, game: Game):
        print('about', flush=True)

    def executeCommand(self, command, game: Game, params):
        try:
            self.commands[command](game)
        except:
            return