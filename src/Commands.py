#!/usr/bin/python3

from src.Game import Game
from src.Parser import Parser
from src.Logic import Logic

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

    def start(self, params, game: Game, logic: Logic):
        if (int(params[0]) == 0):
            print(f'ERROR message - unsupported size or other error', flush=True)
            return
        game.initBoard(int(params[0]))
        print('OK - everything is good', flush=True)

    def turn(self, params, game: Game, logic: Logic):
        game.fillBoard(int(params[0]), int(params[1]), '2')
        game.fillBoard(11, 10, '1')
        x, y = logic.generateRandomPosition()
        print(f'{x},{y}', flush=True)

    def begin(self, params, game: Game, logic: Logic):
        x, y = logic.generateRandomPosition()
        print(f'{x},{y}', flush=True)

    def board(self, params, game: Game, logic: Logic):
        Parse = Parser()
        Parse.askForInput()

        while Parse.getInput().upper() != "DONE":
            coordinate = Parse.getCoordinate()
            game.fillBoard(int(coordinate[0]), int(coordinate[1]), coordinate[2])
            Parse.askForInput()
        x, y = logic.generateRandomPosition()
        print(f'{x},{y}', flush=True)

    def info(self, params, game: Game, logic: Logic):
        print('info', flush=True)

    def about(self, params, game: Game, logic: Logic):
        print('about', flush=True)

    def executeCommand(self, command, params, game: Game, logic: Logic):
        try:
            self.commands[command](params, game, logic)
        except:
            return