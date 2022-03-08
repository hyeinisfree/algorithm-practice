from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.col_set = set() # col
        self.diag_set1 = set() # row-col
        self.diag_set2 = set() # row+col
        self.n = n # length
        
        for x in range(n):
            self.bt(0, x, [])
        
        return self.results
    
    def create_str_row(self, col:int) -> str:
        str_list = ['.'] * self.n
        str_list[col] = 'Q'
        return ''.join(str_list)
    
    def bt(self, row:int, col:int, board:List[str]):
        # exit conditions
        if row==self.n or col==self.n:
            return
        if col in self.col_set:
            return
        diag1_info = row-col
        diag2_info = row+col
        if diag1_info in self.diag_set1:
            return
        if diag2_info in self.diag_set2:
            return
        
        # process
        str_line = self.create_str_row(col)
        board.append(str_line)
    
        if len(board) == self.n:
            self.results.append(board.copy())
            board.pop()
            return
        
        # duplicates sets
        self.col_set.add(col)
        self.diag_set1.add(diag1_info)
        self.diag_set2.add(diag2_info)
        
        # recursive calls
        for x in range(self.n):
            self.bt(row+1, x, board)
        
        # duplicates sets pop
        self.diag_set2.remove(diag2_info)
        self.diag_set1.remove(diag1_info)
        self.col_set.remove(col)
        board.pop()
        
nQsolver = Solution()
nQsolver.solveNQueens(6)