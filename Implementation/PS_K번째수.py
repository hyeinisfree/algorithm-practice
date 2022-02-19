def solution1(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

def solution2(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    return answer