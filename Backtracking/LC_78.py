from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subsets = []
        
        self.bt(0, [])
        
        return self.subsets
    
    def bt(self, index: int, crnt_set: List[int]):
        if index == len(self.nums):
            self.subsets.append(crnt_set.copy())
            return

        num = self.nums[index]
        self.bt(index+1, crnt_set)

        crnt_set.append(num)
        self.bt(index+1, crnt_set)
        crnt_set.pop()