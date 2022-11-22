#!/usr/bin/python3

from src.Parser import Parser
from src.Commands import Commands
from src.Game import Game
from src.Logic import Logic

if __name__ == '__main__':
    Parser = Parser()
    Commands = Commands()
    Game = Game()
    Logic = Logic()

    try:
        Parser.askForInput()

        while Parser.getInput().upper() != "END":
            Commands.executeCommand(Parser.getInput().upper(), Parser.getParams(), Game, Logic)
            Parser.askForInput()
    except KeyboardInterrupt:
        print("\nCTRL+C pressed, exiting..")
        exit(0)