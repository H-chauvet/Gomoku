#!/usr/bin/python3

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
    
    def getParams(self):
        return (self.params)