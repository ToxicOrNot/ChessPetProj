import math
import numpy as np
from boardFile import board
from pieces import Piece

board.placePiece(5, 0, Piece("white", "pawn"))



for x in range(8):
    for y in range(8):
        print(board.getPiece(x, y), end=" ")
    print("")