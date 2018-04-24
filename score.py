#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Score():
    def __init__(self):
        self.points = 0

    def addPoints(self, bonus):
        self.points += bonus * 100