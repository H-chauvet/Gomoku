#!/usr/bin/python3

from src.Parser import Parser
from src.Commands import Commands

if __name__ == '__main__':
    Parser = Parser()
    Commands = Commands()
    Parser.askForInput()

    while Parser.getInput().upper() != "END":
        Commands.executeCommand(Parser.getInput(), '')
        Parser.askForInput()