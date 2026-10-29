import math
import numpy as np
from boardFile import board
from pieces import Piece, Rook

board.placePiece(5, 0, Piece("white", "pawn"))

board.placePiece(2, 0, Rook("white", "rook"))

board.movePiece(2, 0, 7, 0)


for x in range(8):
    for y in range(8):
        print(board.getPiece(x, y), end=" ")
    print("")