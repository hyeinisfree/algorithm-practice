def dfs(depth):
  global result
  if depth == N:
    total = sum(abs(picked[i]-picked[i+1]) for i in range(N-1))
    result = max(result, total)
  for i in range(N):
    if check[i]:
      continue
    picked.append(nums[i])
    check[i] = 1
    dfs(depth+1)
    picked.pop()
    check[i] = 0

N = int(input())
nums = list(map(int, input().split()))
picked, result = [], 0
check = [0] * N
dfs(0)
print(result)