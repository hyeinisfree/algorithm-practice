from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = range(1, n+1)
        output = []

        def BT(level, chosen):
            if level == k:
                output.append(chosen.copy())
                return
            for i in range(level, len(arr)):
                chosen.append(arr[i])
                BT(i+1, chosen)
                chosen.pop()

        BT(0, [])
        return output