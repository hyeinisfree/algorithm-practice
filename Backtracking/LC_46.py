from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def BT(level, chosen):
            if level == len(nums):
                output.append(chosen.copy())
                return
            for i in nums:
                if i not in chosen:
                    chosen.append(i)
                    BT(level+1, chosen)
                    chosen.pop()

        BT(0, [])
        return output