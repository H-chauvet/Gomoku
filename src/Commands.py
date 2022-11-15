#!/usr/bin/python3

class Commands:

    def start(self):
        print('start', flush=True)

    def turn(self):
        print('turn', flush=True)

    def begin(self):
        print('begin', flush=True)

    def board(self):
        print('board', flush=True)

    def info(self):
        print('info', flush=True)

    def end(self):
        print('end', flush=True)

    def about(self):
        print('about', flush=True)

    def __init__(self):
        self.commands = {
            'start': self.start,
            'turn': self.turn,
            'begin': self.begin,
            'board': self.board,
            'info': self.info,
            'end': self.end,
            'about': self.about,
        }

    def executeCommand(self, command, params):
        try:
            self.commands[command]()
        except:
            print('Unknown command', flush=True)