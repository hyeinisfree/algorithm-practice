from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def check_row(row, num):
            for x in range(0,9):
                if board[row][x]==num:
                    return False
            return True

        def check_col(col, num):
            for y in range(0,9):
                if board[y][col]==num:
                    return False
            return True

        def check_box(row, col, num):
            box_x = int(col/3)*3
            box_y = int(row/3)*3
            for y in range(box_y, box_y+3):
                for x in range(box_x, box_x+3):
                    if board[y][x]==num:
                        return False
            return True

        def find_next_empty():
            for y in range(9):
                for x in range(9):
                    if board[y][x] == '.':
                        return [y,x]
            return [9,9]

        def bt(row, col, num):
            if not check_row(row, num):
                return False
            elif not check_col(col, num):
                return False
            elif not check_box(row, col, num):
                return False

            board[row][col] = str(num)
            next_row, next_col = find_next_empty()

            if next_row==9 and next_col==9:
                return True

            for next_num in range(1,10):
                if bt(next_row, next_col, str(next_num)):
                    return True

            board[row][col] = '.'
            return False

        next_row, next_col = find_next_empty()
        if next_row==9 and next_col==9:
            return

        for i in range(1,10):
            bt(next_row, next_col, str(i))
