from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_count = n
        close_count = n
        
        self.result = []
        self.bt(open_count, close_count, '')
        
        return self.result
        
    def bt(self, open_count:int, close_count:int, letters:str):
        if open_count == 0 and close_count == 0:
            self.result.append(letters)
            return
        
        if open_count > 0:
            self.bt(open_count-1, close_count, letters+'(')
        
        if open_count < close_count:
            self.bt(open_count, close_count-1, letters+')')

solution = Solution()
print(solution.generateParenthesis(3))