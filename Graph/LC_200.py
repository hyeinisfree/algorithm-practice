from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.dx = [0, 1, 0, -1] # 아래, 오른쪽, 위, 왼쪽
        self.dy = [1, 0, -1, 0]

        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.count = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if not self.visited[y][x] and grid[y][x] == '1':
                    self.dfs(y, x)
                    self.count += 1
                    
        return self.count
        
    def dfs(self, row, col):
        self.visited[row][col] = True
        
        for i in range(4):
            next_row = int(row + self.dy[i])
            next_col = int(col + self.dx[i])
            
            if next_row < 0 or next_row >= len(self.grid):
                continue
            if next_col < 0 or next_col >= len(self.grid[0]):
                continue
            if self.grid[next_row][next_col] == '0':
                continue
            
            if not self.visited[next_row][next_col]:
                self.dfs(next_row, next_col)
        return