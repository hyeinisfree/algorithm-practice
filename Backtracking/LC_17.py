from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    
        if len(digits) == 0:
            return []
    
        self.digits = digits = digits
        self.comb = []
        self.bt(0, '')
        
        return self.comb
    
    def bt(self, index: int, crntStr: str):
        if index == len(self.digits):
            self.comb.append(crntStr)
            return
        
        num = int(self.digits[index])
        chars = self.keypad[num]
        for char in chars:
            self.bt(index+1, crntStr+char)