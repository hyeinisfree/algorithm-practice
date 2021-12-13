
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    return answer

# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer