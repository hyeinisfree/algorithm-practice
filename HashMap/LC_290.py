from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_map = {}
        word_map = {}
        
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        for idx, c in enumerate(pattern):
            word = words[idx]
            if c not in char_map:
                if word in word_map:
                    return False
                
                else:
                    char_map[c] = word
                    word_map[word] = c
                    
            else:
                if char_map[c] != word:
                    return False
                    
        return True