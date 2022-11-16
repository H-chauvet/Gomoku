#!/usr/bin/python3
from sys import stdin

class Parser:
    def __init__(self):
        self.args = None
        self.commands = None
        self.params = list()

    def askForInput(self):
        self.args = input()
    
    def getInput(self):
        self.commands = self.args.split(" ")[0]
        self.params = self.args.strip(self.commands).split(",")
        self.params = [x.strip(' ') for x in self.params]
        return (self.commands)

    def getCoordinate(self):
        coordinate: list[str] = self.commands.split(",")
        return (coordinate)

    def getParams(self):
        return (self.params)