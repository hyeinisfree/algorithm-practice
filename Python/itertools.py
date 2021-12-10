# itertools
from itertools import combinations_with_replacement, permutations, combinations, product

data = ['A', 'B', 'C'] # 데이터 준비

result1 = list(permutations(data, 3))
print(result1)

result2 = list(combinations(data, 2))
print(result2)

result3 = list(product(data, repeat = 2))
print(result3)

result4 = list(combinations_with_replacement(data, 2))
print(result4)