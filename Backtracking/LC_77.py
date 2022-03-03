class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = range(1, n+1)
        used = [False] * len(arr)
        output = []

        def BT(level, chosen):
            if level == k:
                output.append(chosen.copy())
                return
            for i in range(level, len(arr)):
                if not used[i]:
                    chosen.append(arr[i])
                    used[i] = True
                    BT(i+1, chosen)
                    used[i] = False
                    chosen.pop()

        BT(0, [])
        return output