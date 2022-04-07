from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(neededTime) <= 1:
            return 0
        
        last_char = ""
        max_time = 0
        total_time = 0
        
        for idx,nth_time in enumerate(neededTime):
            nth_char = colors[idx]
            if nth_char != last_char:
                last_char = nth_char
                max_time = nth_time
            else:
                if nth_time <= max_time:
                    total_time += nth_time
                else:
                    total_time += max_time
                    max_time = nth_time
        
        return total_time
        
solution = Solution()
print(solution.minCost("abaac", [1,2,3,4,5]))