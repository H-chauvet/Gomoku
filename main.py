#!/usr/bin/python3

from src.Parser import Parser
from src.Commands import Commands
from src.Game import Game

if __name__ == '__main__':
    Parser = Parser()
    Commands = Commands()
    Game = Game()

    Parser.askForInput()

    while Parser.getInput().upper() != "END":
        Commands.executeCommand(Parser.getInput(), Game, '')
        Parser.askForInput()