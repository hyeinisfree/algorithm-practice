from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_cost = inf
        dp_array = [-1] * (amount+1)
        dp_array[0] = 0
        
        for idx in range(amount+1):
            if dp_array[idx] != -1:
                continue
            
            crnt_min = max_cost
            for coin in coins:
                last_idx = idx - coin
                if last_idx < 0:
                    continue
                last_cost = dp_array[last_idx]
                if last_cost == -1:
                    continue
                cost = last_cost + 1
                crnt_min = min(cost,crnt_min)
                
            dp_array[idx] = -1 if crnt_min==max_cost else crnt_min
            
        return dp_array[amount]

solution = Solution()
print(solution.coinChange(coins=[2,3,5], amount = 10))