from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        answer = image.copy()
        
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        
        visited = []
        queue = []
        
        visited.append([sr, sc])
        queue.append([sr, sc])
    
        while queue:        
            r, c = queue.pop(0)
            originColor = image[r][c]
            
            answer[r][c] = newColor
            
            for i in range(4):
                next_row = r + dy[i]
                next_col = c + dx[i]
                
                if next_row < 0 or next_col < 0:
                    continue
                if next_row >= len(image) or next_col >= len(image[0]):
                    continue
                if image[next_row][next_col] != originColor:
                    continue
                
                if [next_row, next_col] not in visited:
                    visited.append([next_row, next_col])
                    queue.append([next_row, next_col])
        
        return answer
    
solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))