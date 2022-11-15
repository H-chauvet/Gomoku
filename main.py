#!/usr/bin/python3

from src.Parser import Parser

if __name__ == '__main__':
    Parser = Parser()
    Parser.askForInput()
    
    while Parser.getInput().upper() != "END":
        print("Input is : %s" % Parser.getInput())
        Parser.askForInput()