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
        if (int(params[0]) < 5):
            print(f'ERROR Board size incorrect', flush=True)
            return
        game.initBoard(int(params[0]))
        print('OK', flush=True)

    def turn(self, params, game: Game, logic: Logic):
        game.fillBoard(int(params[0]), int(params[1]), '2')
        x, y = logic.getBestMove(game)
        game.fillBoard(x, y, '1')
        print(f'{x},{y}', flush=True)

    def begin(self, params, game: Game, logic: Logic):
        x = game.getBoardSize() / 2
        y = game.getBoardSize() / 2
        print(f'{x},{y}', flush=True)

    def board(self, params, game: Game, logic: Logic):
        Parse = Parser()
        Parse.askForInput()

        while Parse.getInput().upper() != "DONE":
            coordinate = Parse.getCoordinate()
            game.fillBoard(int(coordinate[0]), int(coordinate[1]), coordinate[2])
            Parse.askForInput()
        x, y = logic.getBestMove(game)
        print(f'{x},{y}', flush=True)

    def info(self, params, game: Game, logic: Logic):
        return

    def about(self, params, game: Game, logic: Logic):
        print('about', flush=True)

    def executeCommand(self, command, params, game: Game, logic: Logic):
        self.commands[command](params, game, logic)