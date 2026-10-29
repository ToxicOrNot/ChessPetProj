
class Board:
    def __init__(self):
        self.board = [[None for j in range(8)] for i in range(8)]

    def getPieceInfo(self, x, y):
        if self.board[y][x] is not None:
            return self.board[y][x].color + " " + self.board[y][x].name
        else: return None

    def getPiece(self, x, y):
        return self.board[y][x]

    def placePiece(self, x, y, piece):
        self.board[y][x] = piece



    def movePiece(self, x, y, destx, desty):
        if destx > 7 or desty > 7 or destx < 0 or desty < 0 or x < 0 or y < 0 or x > 7 or y > 7:
            print("Illegal move")
            return 1
        elif self.getPiece(x, y) is None:
            print("Piece not found")
            return 1
        elif not self.getPiece(x, y).check_move(x, y, destx, desty, self):
            print("Illegal move")
            return 1
        if self.getPiece(destx, desty) is not None:
            if self.getPiece(destx, desty).color == self.getPiece(x, y).color:
                print("Illegal move")
                return 1

        self.placePiece(destx, desty, self.getPiece(x, y))
        self.placePiece(x, y, None)
        return 0

board = Board()