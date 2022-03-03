# Recursion
def comb1(arr, r):
    arr.sort()
    used = [False] * len(arr)
    output = []
    
    def generate(level, chosen, used):
        if len(chosen) == r:
            output.append(chosen[:])
            return
        for i in range(level, len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = True
                generate(i+1, chosen, used)
                used[i] = False
                chosen.pop()
        
    generate(0, [], used)
    return output

def comb2(arr, r):
    result = []
    
    if r == 0:
        return [[]]
    
    for i in range(len(arr)):
        for j in comb2(arr[i+1:], r-1):
            result.append([arr[i]]+j)
        
    return result

# Generator
def comb3(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in comb3(arr[i+1:], r-1):
                yield [arr[i]] + next

print(comb1([1,2,3,4],2))
print(comb2([1,2,3,4],2))
print(list(comb3([1,2,3,4],2)))