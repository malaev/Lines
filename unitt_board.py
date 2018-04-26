import unittest
from board import Board

boardFirst = Board()
boardSecond = Board()
boardHorizontal = Board()
boardVertical = Board()

boardFirst.board[0][0] = 2
boardSecond.board[8][8] = 2
for elem in boardHorizontal.board[3]:
    elem = 1;
for i in range(0, 9):
    boardVertical.board[4][i] = 3

class BoardTests(unittest.TestCase):
    def testStep(self):
        boardFirst.step(0, 0, 8, 8, 2)
        self.assertEqual(boardFirst.board, boardSecond.board)

    def testNextIteration(self):
        board = Board()
        for i in range(0, 27):
            board.nextIteration()

        for line in board.board:
            for elem in line:
                if (elem == 0):
                    self.assertEqual(True, False)
        self.assertEqual(True, True)

    def testHorizontalLine(self):
        emptyBoard = Board()
        boardHorizontal.lineExist()
        self.assertEqual(boardHorizontal.board, emptyBoard.board)

    def testVerticalLine(self):
        emptyBoard = Board()
        boardVertical.lineExist()
        self.assertEqual(boardVertical.board, emptyBoard.board)