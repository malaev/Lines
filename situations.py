#!/usr/bin/python3
# -*- coding: utf-8 -*-

def valideVertex(x, y):
    return x >= 0 & x < 10 & y >= 0 & y < 10

def valideStep(board, startX, startY, endX, endY):
    visited, queue = set(), [(startX, startY)]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if (valideVertex(vertex[0] + 1, vertex[1])):
                queue.add(vertex[0] + 1, vertex[1])
            if (valideVertex(vertex[0] - 1, vertex[1])):
                queue.add(vertex[0] - 1, vertex[1])
            if (valideVertex(vertex[0], vertex[1] + 1)):
                queue.add(vertex[0], vertex[1] + 1)
            if (valideVertex(vertex[0], vertex[1] - 1)):
                queue.add(vertex[0], vertex[1] - 1)
    return (endX, endY) in visited