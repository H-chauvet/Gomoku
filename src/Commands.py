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

    def check_param(nb_param, params):
        if nb_param == 4:
            if (len(params) != nb_param - 2):
                return False
        else:
            new_list = params[0].split(' ')
            if (new_list[0] == ''):
                if (nb_param != 0):
                    return False
            elif (len(new_list) != nb_param):
                return False  
        return True

    def start(self, params, game: Game, logic: Logic):
        if (Commands.check_param(1, params) == False):
            return
        if (int(params[0]) < 5):
            print(f'ERROR Board size incorrect', flush=True)
            return
        game.initBoard(int(params[0]))
        print('OK', flush=True)

    def turn(self, params, game: Game, logic: Logic):
        if (Commands.check_param(4, params) == False):
            return
        game.fillBoard(int(params[0]), int(params[1]), '2')
        x, y = logic.getBestMove(game)
        game.fillBoard(x, y, '1')
        print(f'{x},{y}', flush=True)

    def begin(self, params, game: Game, logic: Logic):
        if (Commands.check_param(0, params) == False):
            return
        x = game.getBoardSize() / 2
        y = game.getBoardSize() / 2
        print(f'{x},{y}', flush=True)

    def board(self, params, game: Game, logic: Logic):
        if (Commands.check_param(0, params) == False):
            return
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
        if (Commands.check_param(0, params) == False):
            return
        print('name="Best IA", version="1.0", author="The Group", country="France"', flush=True)

    def executeCommand(self, command, params, game: Game, logic: Logic):
        if (command != "START" and command != "TURN" and command != "BEGIN" and command != "BOARD" and command != "INFO" and command != "ABOUT"):
            print("Command not found")
            return
        self.commands[command](params, game, logic)