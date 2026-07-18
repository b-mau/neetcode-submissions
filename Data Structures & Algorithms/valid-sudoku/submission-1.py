from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in board:
            current_row = set()
            for elem in row:
                if elem == ".":
                    continue
                if elem not in current_row:
                    current_row.add(elem)
                else:
                    return False
        
        # column check
        for i in range(9):
            current_column = set()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] not in current_column:
                    current_column.add(row[i])
                else:
                    return False

        # square check
        for i in range(9):
            current_square = set()
            for j in range(9):
                row_idx = (i // 3) * 3 + (j // 3)
                col_idx = (i % 3) * 3 + (j % 3)

                elem = board[row_idx][col_idx]
                if elem == ".":
                    continue
                if elem not in current_square:
                    current_square.add(elem)
                else:
                    return False

        return True