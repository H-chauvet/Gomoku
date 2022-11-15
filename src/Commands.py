#!/usr/bin/python3

from src.Game import Game
from src.Parser import Parser

class Commands:

    def __init__(self):
        self.commands = {
            'START': self.start,
            'TURN': self.turn,
            'BEGIN': self.begin,
            'BOARD': self.board,
            'INFO': self.info,
            'ABOUT': self.about,
        }

    def start(self, params, game: Game):
        game.initBoard(int(params[0]))
        print('OK - everything is good', flush=True)

    def turn(self, params, game: Game):
        game.fillBoard(int(params[0]), int(params[1]), '2')
        game.fillBoard(11, 10, '1')
        print('11,10', flush=True)

    def begin(self, params, game: Game):
        print('10,10', flush=True)

    def board(self, params, game: Game):
        Parse = Parser()
        Parse.askForInput()

        while Parse.getInput().upper() != "DONE":
            coordinate = Parse.getCoordinate()
            game.fillBoard(int(coordinate[0]), int(coordinate[1]), coordinate[2])
            Parse.askForInput()
        print('9,9', flush=True)

    def info(self, params, game: Game):
        print('info', flush=True)

    def about(self, params, game: Game):
        print('about', flush=True)

    def executeCommand(self, command, params, game: Game):
        try:
            self.commands[command](params, game)
        except:
            return