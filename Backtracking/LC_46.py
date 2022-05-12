from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.perms = []
        
        self.bt([])
        return self.perms
    
    def bt(self, crnt_set: List[int]):
        if len(crnt_set) == len(self.nums):
            self.perms.append(crnt_set.copy())
            return
        
        for num in self.nums:
            if num in crnt_set:
                continue
            
            crnt_set.append(num)
            self.bt(crnt_set)
            crnt_set.pop()