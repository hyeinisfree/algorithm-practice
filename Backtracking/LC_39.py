from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.combs = []
        
        self.bt(0, target, [])
        return self.combs
    
    def bt(self, prevIdx: int, targetSum: int, comb:List[int]):
        # exit conditions
        if targetSum == 0:
            self.combs.append(comb.copy())
            return
        elif targetSum < 0:
            return
        
        # process(candidates filtering)
        for idx in range(prevIdx, len(self.candidates)):
            num = self.candidates[idx]
            
            # recursion call
            comb.append(num)
            self.bt(idx, targetSum-num, comb)
            comb.pop()