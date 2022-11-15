#!/usr/bin/python3

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

COMMANDS = {
    "start": start,
    "turn": turn,
    "begin": begin,
    "board": board,
    "info": info,
    "end": end,
    "about": about,
}

if __name__ == '__main__':
    COMMANDS['start']()