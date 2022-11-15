#!/usr/bin/python3

class Parser:
    def __init__(self):
        self.args = None

    def askForInput(self):
        self.args = input()
    
    def getInput(self):
        return self.args