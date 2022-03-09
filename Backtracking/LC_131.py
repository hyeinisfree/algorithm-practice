from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        self.s = s
        self.results = []
        
        for idx in range(len(s)):
            self.bt(0, idx, [])
        
        return self.results
    
    def is_palindrome(self, begin:int, last:int) -> bool:
        while(begin<last):
            if self.s[begin] != self.s[last]:
                return False
            begin += 1
            last -= 1
        return True
        
    def bt(self, begin:int, last:int, letters:List[str]): 
        is_palindrome = self.is_palindrome(begin, last)
        
        if not is_palindrome:
            return
        
        letters.append(self.s[begin:last+1])
        if len(self.s) == last+1:
            self.results.append(letters.copy())
            letters.pop()
            return
        
        for idx in range(last+1, len(self.s)):
            self.bt(last+1, idx, letters)
        
        letters.pop()
        return
        
solution = Solution()
print(solution.partition("bb"))