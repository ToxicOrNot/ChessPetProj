
class Piece:
    def __init__(self, color, id):
        self.color = color
        self.name = id

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