from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        
        next_row, next_col = self.find_next_empty()
        if next_row==9 and next_col==9:
            return

        for i in range(1,10):
            self.bt(next_row, next_col, str(i))

    def check_row(self, row:int, num:str) -> bool:
        for x in range(0,9):
            if self.board[row][x]==num:
                return False
        return True

    def check_col(self, col:int, num:str) -> bool:
        for y in range(0,9):
            if self.board[y][col]==num:
                return False
        return True

    def check_box(self, row:int, col:int, num:str) -> bool:
        box_x = int(col/3)*3
        box_y = int(row/3)*3
        for y in range(box_y, box_y+3):
            for x in range(box_x, box_x+3):
                if self.board[y][x]==num:
                    return False
        return True

    def find_next_empty(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == '.':
                    return [y,x]
        return [9,9]

    def bt(self, row:int, col:int, num:str) -> bool:
        if not self.check_row(row, num):
            return False
        elif not self.check_col(col, num):
            return False
        elif not self.check_box(row, col, num):
            return False

        self.board[row][col] = str(num)
        next_row, next_col = self.find_next_empty()

        if next_row==9 and next_col==9:
            return True

        for next_num in range(1,10):
            if self.bt(next_row, next_col, str(next_num)):
                return True

        self.board[row][col] = '.'
        return False