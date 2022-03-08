from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        output = []
        
        if len(digits) == 0:
            return []

        def BT(index, letter):
            if index == len(digits):
                output.append(letter)
                return

            num = int(digits[index])
            chars = keypad[num]
            for c in chars:
                BT(index+1, letter+c)
        
        BT(0, '')
        return output