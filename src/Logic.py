#!/usr/bin/python3

import random

class Logic:

    def __init__(self):
        self.x = 0
        self.y = 0

    def generateRandomPosition(self):
        self.x = random.randint(0, 20)
        self.y = random.randint(0, 20)
        return ((self.x, self.y))