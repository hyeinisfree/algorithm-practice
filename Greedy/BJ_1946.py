import sys

t = int(input())
for i in range(t):
  n = int(input())
  array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  array.sort()
  
  cnt = 1
  min = array[0][1]
  for j in array[1:]:
    if j[1] < min:
      cnt += 1
      min = j[1]
  
  print(cnt)