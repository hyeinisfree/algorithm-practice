from itertools import combinations
import math

def solution(nums):
    answer = 0
    data = list(combinations(nums, 3))
    for i in data:
        n = sum(i)
        if is_prime(n):
            answer += 1
    return answer
    
def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True