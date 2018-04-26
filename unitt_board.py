import unittest
from board import Board

boardFirst = Board()
boardSecond = Board()
boardWithLine = Board()

boardFirst.board[0][0] = 2
boardSecond.board[8][8] = 2
boardWithLine[3] = [1, 1, 1, 1, 1, 1, 1, 1, 1]

class BoardTests(unittest.TestCase):
    def testStep(self):
        self.assertEqual(Board.step(boardFirst, 0, 0, 8, 8, 2), boardSecond.board)

    def nextIterationTest(self):
        board = Board()
        for i in range(0, 27):
            board.nextIteration()

        for line in board.board:
            for elem in line:
                if (elem == 0):
                    self.assertEqual(True, False)
        self.assertEqual(True, True)

    def lineTest(self):
        emptyBoard = Board()
        self.assertEqual(Board.lineExist(boardWithLine), emptyBoard.board)