n = int(input())
p = list(map(int, input().split()))

s = sorted(p)

result = 0

for i in s:
  result += i * n
  n -= 1

print(result)