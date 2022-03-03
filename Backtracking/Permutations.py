# Recursion
def perm1(arr, r):
    arr.sort()
    used = [False] * len(arr)
    output = []
    
    def generate(chosen):
        if len(chosen) == r:
            output.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = True
                generate(chosen)
                used[i] = False
                chosen.pop()

    generate([])
    return output

# Swap
def perm2(arr, r):
    arr.sort()
    output = []
    
    def generate(level):
        if level == r:
            output.append(arr[:r])
            return
        for i in range(level, len(arr)):
            arr[i], arr[level] = arr[level], arr[i]
            generate(level+1)
            arr[i], arr[level] = arr[level], arr[i]
            
    generate(0)
    return output

# Generator
def perm3(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in perm3(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

# While                
def perm4(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
                
print(perm1([1,2,3],3))
print(perm2([1,2,3],3))
print(list(perm3([1,2,3],3)))
print(perm4([1,2,3]))