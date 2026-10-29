import math
import numpy as np
from boardFile import board
from pieces import Piece, Rook

board.placePiece(0, 5, Piece("black", 1))

board.placePiece(0, 2, Rook("white", "queenSide"))

board.movePiece(0, 2, 1, 5)


for y in range(8):
    for x in range(8):
        print(board.getPiece(x, y), end=" ")
    print("")