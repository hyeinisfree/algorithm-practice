from collections import Counter

def solution(N, stages):
    answer = []
    
    total = dict.fromkeys([x for x in range(1, N+1)], 0)
    for i in range(1, N+1):
        for j in stages:
            if i <= j:
                total[i] += 1
    counter = dict(Counter(stages))
    
    fail = dict.fromkeys([x for x in range(1, N+1)], 0)
    for i in range(1, N+1):
        if total[i] != 0 and i in counter:
            fail[i] = counter[i]/total[i]
            
    answer = sorted(fail.items(), key = lambda item: item[1], reverse = True)
    answer = list(map(lambda x: x[0], answer))
    return answer

# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)

# def solution(N, stages):
#     fail = {}
#     for i in range(1,N+1):
#         try:
#             fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
#         except:
#             fail_ = 0
#         fail[i]=fail_
#     answer = sorted(fail, key=fail.get, reverse=True)
#     return answer