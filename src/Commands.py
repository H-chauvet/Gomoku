#!/usr/bin/python3

class Commands:

    def start():
        print('start')

    def turn():
        print('turn')

    def begin():
        print('begin')

    def board():
        print('board')

    def info():
        print('info')

    def end():
        print('end')

    def about():
        print('about')

    def __init__(self):
        self.commands = {
            "start": self.start,
            "turn": self.turn,
            "begin": self.begin,
            "board": self.board,
            "info": self.info,
            "end": self.end,
            "about": self.about,
        }

    def executeCommand(self, command, params):
        self.commands[command](params)