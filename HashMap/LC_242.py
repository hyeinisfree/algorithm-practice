from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        
        for c in s:
            count = table.get(c)
            if count is None:
                table[c] = 1
                continue
            
            table[c] += 1
            
        for c in t:
            count = table.get(c)
            if count is None:
                return False
            
            table[c] -= 1
            
        for key, value in table.items():
            if value != 0:
                return False
            
        return True