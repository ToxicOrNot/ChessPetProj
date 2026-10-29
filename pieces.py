import numpy as np

class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

class Rook(Piece):
    def check_move(self, source_x, source_y, dest_x, dest_y, board):
        if source_y == dest_y and source_x == dest_x:
            return False
        if source_y == dest_y:
            step = 1 if source_x < dest_x else -1
            for i in range (source_x + step, dest_x, step):
                if board.getPiece(i, source_y) is not None:
                    return False
            return True
        elif source_x == dest_x:
            step = 1 if source_y < dest_y else -1
            for i in range (source_y + step, dest_y, step):
                if board.getPiece(source_x, i) is not None:
                    return False
            return True
        else:
            return False


class Bishop(Piece):
    def check_move(self, source_x, source_y, dest_x, dest_y, board):
        changex = dest_x - source_x
        changey = dest_y - source_y
        stepx = np.sign(changex)
        stepy = np.sign(changey)
        row = source_y + stepy
        if changex == changey == 0:
            return False
        if abs(changex) != abs(changey):
            return False
        for i in range (source_x + stepx, dest_x, stepx):
            if board.getPiece(i, row) is not None:
                return False
            row += stepy
        return True