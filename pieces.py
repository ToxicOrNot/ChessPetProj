
class Piece:
    def __init__(self, color, id):
        self.color = color
        self.name = id

class Rook(Piece):
    def check_move(self, source_row, source_col, dest_row, dest_col, board):
        if source_row == dest_row and source_col == dest_col:
            return False
        if source_row == dest_row:
            step = 1 if source_col < dest_col else -1
            for i in range (source_col + step, dest_col, step):
                if board.getPiece(source_row, i) is not None:
                    return False
            return True
        elif source_col == dest_col:
            step = 1 if source_row < dest_row else -1
            for i in range (source_row + step, dest_row, step):
                if board.getPiece(i, source_col) is not None:
                    return False
            return True
        else:
            return False