#!/usr/bin/python3

"""! Parser class"""
class Parser:
    def __init__(self):
        """! Initializes the the parser. """
        
        self.args = None
        self.commands = None
        self.params = list()

    def askForInput(self):
        """! Get user input."""
        
        self.args = input()
        
    def getInput(self) -> str:
        """! Parsing the user input."""
        
        self.commands = self.args.split(" ")[0]
        self.params = self.args.strip(self.commands).split(",")
        self.params = [x.strip(' ') for x in self.params]
        return (self.commands)

    def getCoordinate(self):
        """! Parsing the values for coordinates."""
        
        coordinate: list[str] = self.commands.split(",")
        return (coordinate)
    def getParams(self):
        """! Get params of the user input."""
        
        return (self.params)