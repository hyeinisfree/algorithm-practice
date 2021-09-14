import sys
import itertools
input = sys.stdin.readline

N = int(input())
for x in itertools.permutations(range(1, N+1)):
  for i in x:
    print(i, end=' ')
  print()