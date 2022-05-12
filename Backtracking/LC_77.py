from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.nums = range(1, n+1)
        self.combs = []

        self.bt(0, [])
        return self.combs

    def bt(self, index: int, chosen: List[int]):
        if len(chosen) == self.k:
            self.combs.append(chosen.copy())
            return
        
        for i in range(index, self.n):
            chosen.append(self.nums[i])
            self.bt(i+1, chosen)
            chosen.pop()