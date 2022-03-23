from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minCost2d = a = [[0] * cols for i in range(rows)]
        
        #initialize 2d cost map
        minCost2d[0][0] = grid[0][0]
        for colIdx in range(1,cols):
            minCost2d[0][colIdx] = grid[0][colIdx] + minCost2d[0][colIdx-1]
        for rowIdx in range(1,rows):
            minCost2d[rowIdx][0] = grid[rowIdx][0] + minCost2d[rowIdx-1][0]
        
        #bottom up DP
        for rowIdx in range (1,rows):
            for colIdx in range (1,cols):
                prevCol = colIdx - 1
                prevRow = rowIdx - 1
                
                upCost = minCost2d[prevRow][colIdx]
                leftCost = minCost2d[rowIdx][prevCol]
                
                prevCost = min(upCost,leftCost)
                cost = prevCost + grid[rowIdx][colIdx]        
                minCost2d[rowIdx][colIdx] = cost
                    
        minCost = minCost2d[rows-1][cols-1]    
        return minCost