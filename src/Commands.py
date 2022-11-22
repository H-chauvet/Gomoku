#!/usr/bin/python3

from src.Game import Game
from src.Parser import Parser
from src.Logic import Logic

"""! Commands class"""
class Commands:

    def __init__(self):
        """! Initialize the commands. """
        self.commands = {
            'START': self.start,
            'TURN': self.turn,
            'BEGIN': self.begin,
            'BOARD': self.board,
            'INFO': self.info,
            'ABOUT': self.about,
            'DISPLAY': self.display,
        }
        self.size_x = 0
        self.size_y = 0
        self.is_start = False

    def check_param(nb_param: int, params: list) -> bool:
        """! Check if the number of parameters is correct
        @param nb_param Number of parameters
        @param params List of parameters
        """
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

    def start(self, params: list, game: Game, logic: Logic):
        """! Command to start the game
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (Commands.check_param(1, params) == False):
            return
        if (int(params[0]) < 5):
            print(f'ERROR Board size incorrect', flush=True)
            return
        self.size_x = int(params[0])
        self.size_y = int(params[0])
        self.is_start = True
        game.initBoard(int(params[0]))
        print('OK', flush=True)

    def check_coordinate(self, params: list, game: Game, logic: Logic) -> bool:
        """! Check if the coordinates are correct
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (int(params[0]) >= self.size_x or int(params[1]) >= self.size_y):
            print("Coordinate out of range", flush=True)
            return False
        return True

    def turn(self, params: list, game: Game, logic: Logic):
        """! Command to play a turn
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (self.is_start == False):
            print("Game not start", flush=True)
        if (Commands.check_param(4, params) == False):
            return
        if (Commands.check_coordinate(self, params, game, logic) == False):
            return
        game.fillBoard(int(params[0]), int(params[1]), '2')
        x, y = logic.getBestMove(game, self.size_x, self.size_y)
        game.fillBoard(x, y, '1')
        print(f'{x},{y}', flush=True)

    def display(self, params: list, game: Game, logic: Logic):
        """! Command to display the board
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (self.is_start == False):
            print("Game not start", flush=True)
        print(game.board)

    def begin(self, params: list, game: Game, logic: Logic):
        """! Command to begin the game
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (self.is_start == False):
            print("Game not start", flush=True)
        if (Commands.check_param(0, params) == False):
            return
        x = int(game.getBoardSize() / 2)
        y = int(game.getBoardSize() / 2)
        game.fillBoard(x, y, '1')
        print(f'{x},{y}', flush=True)

    def board(self, params: list, game: Game, logic: Logic):
        """! Command to fill the board with given arguments
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (self.is_start == False):
            print("Game not start", flush=True)
        if (Commands.check_param(0, params) == False):
            return
        Parse = Parser()
        Parse.askForInput()

        while Parse.getInput().upper() != "DONE":
            coordinate = Parse.getCoordinate()
            game.fillBoard(int(coordinate[0]), int(coordinate[1]), coordinate[2])
            Parse.askForInput()
        x, y = logic.getBestMove(game, self.size_x, self.size_y)
        game.fillBoard(x, y, '1')
        print(f'{x},{y}', flush=True)

    def info(self, params: list, game: Game, logic: Logic):
        """! Command useless"""
        return

    def about(self, params: list, game: Game, logic: Logic):
        """! Command to display the information about the game"""
        if (Commands.check_param(0, params) == False):
            return
        print('name="Best IA", version="1.0", author="The Group", country="France"', flush=True)

    def executeCommand(self, command: str, params: list, game: Game, logic: Logic):
        """! Execute the command
        @param command Command to execute
        @param params List of parameters
        @param game Game object
        @param logic Logic object
        """
        if (command != "START" and command != "TURN" and command != "BEGIN" and command != "BOARD" and command != "INFO" and command != "ABOUT" and command != "DISPLAY"):
            print("Command not found", flush=True)
            return
        self.commands[command](params, game, logic)