from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        visited = []
        queue = []
        
        visited.append([0,0])
        queue.append([0,0])
        grid[0][0] = 1
        
        dy = [-1,-1,0,1,1,1,0,-1]
        dx = [0,1,1,1,0,-1,-1,-1]
        
        while queue:
            r, c = queue.pop(0)
            now = grid[r][c]
            
            for i in range(8):
                next_row = r + dy[i]
                next_col = c + dx[i]
                if next_row < 0 or next_col < 0:
                    continue
                if next_row >= len(grid) or next_col >= len(grid[0]):
                    continue
                if grid[next_row][next_col] == 0:
                    grid[next_row][next_col] = now + 1
                    visited.append([next_row, next_col])
                    queue.append([next_row, next_col])
        
        if [len(grid)-1,len(grid[0])-1] in visited:
            return grid[len(grid)-1][len(grid[0])-1]
        return -1
    
solution = Solution()
print(solution.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))