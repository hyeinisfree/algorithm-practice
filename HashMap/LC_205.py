from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_length = len(s)
        
        table1 = {}
        table2 = {}
        for idx in range(0, str_length):
            match1 = table1.get(s[idx])
            match2 = table2.get(t[idx])
            if match1 is None and match2 is None:
                table1[s[idx]] = t[idx]
                table2[t[idx]] = s[idx]
                continue
            elif match1 == t[idx] and match2 == s[idx]:
                continue
            
            return False
        return True