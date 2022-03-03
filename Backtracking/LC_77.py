class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = range(1, n+1)
        used = [False] * len(arr)
        output = []

        def generate(level, chosen, used):
            if len(chosen) == k:
                output.append(chosen[:])
                return
            for i in range(level, len(arr)):
                if not used[i]:
                    chosen.append(arr[i])
                    used[i] = True
                    generate(i+1, chosen, used)
                    used[i] = False
                    chosen.pop()

        generate(0, [], used)
        return output