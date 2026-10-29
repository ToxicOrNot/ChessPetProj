
class Board:
    def __init__(self):
        self.board = [[None for j in range(8)] for i in range(8)]

    def getPieceInfo(self, x, y):
        if self.board[x][y] is not None:
            return self.board[x][y].color + " " + self.board[x][y].name
        else: return None

    def getPiece(self, x, y):
        return self.board[x][y]

    def placePiece(self, x, y, piece):
        self.board[x][y] = piece

    def move(self, x, y, destx, desty):
        if self.board[x][y] is None:
            print("Piece not found")
        elif self.board[destx][desty] is not None:
            print("Destination is occupied")
        else:
            self.placePiece(destx, desty, self.getPiece(x, y))
            self.placePiece(x, y, None)

board = Board()