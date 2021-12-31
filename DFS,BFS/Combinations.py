from itertools import combinations

def comb1(arr, n):
  result = []
  
  if n > len(arr):
    return result
  
  if n == 1:
    for i in arr:
      result.append([i])
      
  elif n > 1:
    for i in range(len(arr) - n + 1):
      for j in comb1(arr[i + 1:], n-1):
        result.append([arr[i]] + j)
        
  return result

def comb2(arr, r):
  arr = sorted(arr)
  used = [0 for _ in range(len(arr))]

  def generate(chosen):
    if len(chosen) == r:
      print(chosen)
      return

    start = arr.index(chosen[-1]) + 1 if chosen else 0
    for next in range(start, len(arr)):
      if used[next] == 0 and (next == 0 or arr[next-1] != arr[next] or used[next-1]):
        chosen.append(arr[next])
        used[next] = 1
        generate(chosen)
        chosen.pop()
        used[next] = 0
  generate([])
  
def comb3(arr, r):
  for i in range(len(arr)):
    if r == 1:
      yield [arr[i]]
    else:
      for next in comb3(arr[i+1:], r-1):
        yield [arr[i]] + next


arr = [1, 2, 3, 4, 5]

print(comb1(arr, 3))
comb2(arr, 3)
print(list(comb3(arr, 3)))

print(list(combinations(arr, 3)))