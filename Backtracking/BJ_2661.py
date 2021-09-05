def dfs(cnt):
  global result
  for i in range(1, (cnt//2) + 1):
    if result[-2 * i:-1 * i] == result[-1 * i:]:
      return -1
  if cnt == N:
    print("".join(result))
    return 0
  for i in range(1, 4):
    result.append(str(i))
    if dfs(cnt + 1) == 0:
      return 0
    result.pop()


N = int(input())
result = []
dfs(0)