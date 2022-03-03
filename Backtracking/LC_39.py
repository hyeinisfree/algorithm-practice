class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        
        def BT(level, chosen, targetSum):
            if targetSum == 0:
                output.append(chosen.copy())
                return
            elif targetSum < 0:
                return
            
            for i in range(level, len(candidates)):
                chosen.append(candidates[i])
                BT(i, chosen, targetSum-candidates[i])
                chosen.pop()
                    
        BT(0, [], target)
        return output