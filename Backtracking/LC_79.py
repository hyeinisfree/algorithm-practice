from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False
        
        self.board = board
        self.word = word
        
        self.dx = [0,1,0,-1] # 위, 오른쪽, 아래, 왼쪽
        self.dy = [-1,0,1,0]
        
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    if len(word) == 1:
                        return True
                    elif self.bt(0, y, x, visited):
                        return True
        return False
        
    def bt(self, idx, row, col, visited):
        if idx == len(self.word)-1:
            if self.board[row][col] != self.word[idx]:
                return False
            return True
        if self.board[row][col] != self.word[idx]:
            return False
        
        visited[row][col] = True
        
        for i in range(4):
            next_row = row + self.dy[i]
            next_col = col + self.dx[i]

            if 0 <= next_row < len(self.board) and 0 <= next_col < len(self.board[0]):
                if not visited[next_row][next_col]:
                    if self.bt(idx+1, next_row, next_col, visited):
                        return True
        
        visited[row][col] = False
        return False