import math

# 시간 복잡도 O(x)
def is_prime_number(x):
  # 2부터 (x - 1)까지의 모든 수를 확인하며
  for i in range(2, x):
    # x가 해당 수로 나누어 떨어진다면
    if x % i == 0:
      return False # 소수가 아님
  return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# 시간 복잡도 O(x의 1/2제곱)
def is_prime_number_improve(x):
  # 2부터 x의 제곱근까지의 모든 수를 확인하며
  for i in range(2, int(math.sqrt(x)) + 1):
    # x가 해당 수로 나누어 떨어진다면
    if x % i == 0:
      return False # 소수가 아님
  return True # 소수임

print(is_prime_number_improve(4))
print(is_prime_number_improve(7))