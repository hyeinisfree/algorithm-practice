# 거스름돈 문제

import sys
input = sys.stdin.readline

money = int(input())
n = 1000 - money

count = 0
coin = [500, 100, 50, 10, 5, 1]
  
for i in coin:
  count += n // i
  n %= i

print(count)