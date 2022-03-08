from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
    
        def BT(index, crnt_set):
            if index == len(nums):
                output.append(crnt_set.copy())
                return

            num = nums[index]
            BT(index+1, crnt_set)

            crnt_set.append(num)
            BT(index+1, crnt_set)
            crnt_set.pop()

        BT(0, [])
        return output  