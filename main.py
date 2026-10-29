import math
import numpy as np
from boardFile import board
from pieces import Piece, Rook

board.placePiece(5, 0, Piece("black", 1))

board.placePiece(2, 0, Rook("white", "queenSide"))

board.movePiece(2, 0, 5, 1)


for x in range(8):
    for y in range(8):
        print(board.getPiece(x, y), end=" ")
    print("")