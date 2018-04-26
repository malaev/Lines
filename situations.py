#!/usr/bin/python3
# -*- coding: utf-8 -*-

def valideVertex(x, y):
    '''Проверка на принадлежность доске'''
    return x >= 0 and x < 9 and y >= 0 and y < 9

def valideStep(board, startX, startY, endX, endY):
    '''Проверка на возможность хода'''
    visited, queue = set(), [(startX, startY)]
    '''bfs для поиска пути от старта до финиша'''
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if (valideVertex(vertex[0] + 1, vertex[1]) and board[vertex[0] + 1][vertex[1]] == 0):
                queue.insert(len(queue) - 1, (vertex[0] + 1, vertex[1]))
            if (valideVertex(vertex[0] - 1, vertex[1]) and board[vertex[0] - 1][vertex[1]] == 0):
                queue.insert(len(queue) - 1, (vertex[0] - 1, vertex[1]))
            if (valideVertex(vertex[0], vertex[1] + 1) and board[vertex[0]][vertex[1] + 1] == 0):
                queue.insert(len(queue) - 1, (vertex[0], vertex[1] + 1))
            if (valideVertex(vertex[0], vertex[1] - 1) and board[vertex[0]][vertex[1] - 1] == 0):
                queue.insert(len(queue) - 1, (vertex[0], vertex[1] - 1))
    return (endX, endY) in visited