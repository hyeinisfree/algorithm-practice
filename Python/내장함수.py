# 내장 함수

# sum()
result1 = sum([1, 2, 3, 4, 5])
print(result1)

# min()
result2 = min(7, 3, 5, 2)
print(result2)

# max()
result3 = max(7, 3, 5, 2)
print(result3)

# eval()
result4 = eval("(3 + 5) * 7")
print(result4)

# sorted()
result5 = sorted([9, 1, 8, 5, 4])
print(result5)

# sorted() - reverse
result6 = sorted([9, 1, 8, 5, 4], reverse = True)
print(result6)

# sorted() - key
result7 = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result7)