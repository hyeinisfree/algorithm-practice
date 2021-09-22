import sys
input = sys.stdin.readline

k = int(input())
sign = input().split()
check = [False] * 10
max, min = "", ""

def poss(i,j,k):
  if k == ">":
    return i>j
  else:
    return i<j


def recu(cnt, s):
  global max,min
  if cnt > k:
    if len(min) == 0:
      min = s
    else:
      max = s
    return
  for i in range(10):
    if check[i] == False:
      if cnt == 0 or poss(s[-1], str(i), sign[cnt-1]):
        check[i] = True
        recu(cnt+1,s+str(i))
        check[i] = False

recu(0, "")
print(max)
print(min)