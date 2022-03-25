from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        str_length = len(s)
        if str_length == 0:
            return 0
        
        dp = [None]*(str_length+1)
        dp[-1] = 1
        
        last_char = s[-1]
        if int(last_char) == 0:
            dp[str_length-1] = 0
        else:
            dp[str_length-1] = 1
            
        for idx in range(str_length-2, -1, -1):
            single_num = int(s[idx])
            single_count = 0
            if single_num > 0:
                single_count = dp[idx+1]
            
            double_num = int(s[idx:idx+2])
            double_count = 0
            if 10 <= double_num <= 26:
                double_count = dp[idx+2]
                
            count = single_count + double_count
            dp[idx] = count
            
        return dp[0]
        
solution = Solution()
print(solution.nemDecodings("212325"))