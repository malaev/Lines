#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
from situations import valideStep
from score import Score

class Board():
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.score = Score()

    def nextIteration(self):
        for i in range(0, 3):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            while(self.board[x][y] != 0):
                x = random.randint(0, 8)
                y = random.randint(0, 8)
            self.board[x][y] = random.randint(1, 7)

    def step(self, startX, startY, endX, endY, color):
        if (valideStep(self.board, startX, startY, endX, endY)):
            self.board[startX][startY] = 0
            self.board[endX][endY] = color

    def lineExist(self):
        count = 0;
        for i in range(0, 9):
            if (count > 4):
                for k in range(j - count, j):
                    self.board[i - 1][k] = 0
                self.score.addPoints(count)
            count = 0
            for j in range(1, 9):
                if (self.board[i][j] == self.board[i][j - 1]):
                    count += 1;
                else:
                    if (count > 4):
                        for k in range(j - count, j):
                            self.board[i][k] = 0
                        self.score.addPoints(count)
        if (count > 4):
            for k in range(j - count, j):
                self.board[8][k] = 0
            self.score.addPoints(count)

        count = 0;
        for j in range(0, 9):
            if (count > 4):
                for k in range(i - count, i):
                    self.board[k][j - 1] = 0
                self.score.addPoints(count)
            count = 0
            for i in range(1, 9):
                if (self.board[i][j] == self.board[i][j - 1]):
                    count += 1;
                else:
                    if (count > 4):
                        for k in range(i - count, i):
                            self.board[k][j] = 0
                        self.score.addPoints(count)
        if (count > 4):
            for k in range(i - count, i):
                self.board[k][8] = 0
            self.score.addPoints(count)


