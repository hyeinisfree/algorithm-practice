from itertools import permutations

def perm1(arr, r):
  result = []
  if r > len(arr):
    return result
  
  if r == 1:
    for i in arr:
      result.append([i])
  elif r > 1:
    for i in range(len(arr)):
      ans = [i for i in arr]
      ans.remove(arr[i])
      for p in perm1(ans, r-1):
        result.append([arr[i]]+p)
  
  return result

def perm2(arr, r):
  arr = sorted(arr)
  used = [0 for _ in range(len(arr))]
  
  def generate(chosen, used):
    if len(chosen) == r:
      print(chosen)
      return
    
    for i in range(len(arr)):
      if not used[i]:
        chosen.append(arr[i])
        used[i] = 1
        generate(chosen, used)
        used[i] = 0
        chosen.pop()
  generate([], used)
  
def perm3(array, r):
  for i in range(len(array)):
    if r == 1:
      yield [array[i]]
    else:
      for next in perm3(array[:i]+array[i+1:], r-1):
        yield [array[i]] + next


arr = [1, 2, 3, 4, 5]

print(perm1(arr, 2))
perm2(arr, 2)
print(list(perm3(arr, 2)))

print(list(permutations(arr, 2)))