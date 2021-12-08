from collections import deque

def solution(numbers, hand):
    answer = []
    
    phone = {
      1 : (0, 0),
      2 : (0, 1),
      3 : (0, 2),
      4 : (1, 0),
      5 : (1, 1),
      6 : (1, 2),
      7 : (2, 0),
      8 : (2, 1),
      9 : (2, 2),
      '*' : (3, 0),
      0 : (3, 1),
      '#' : (3, 2),
    }
    
    just_left = [1, 4, 7]
    just_right = [3, 6, 9]
    
    lnow = phone['*']
    rnow = phone['#']
    
    for i in numbers:
      if i in just_left:
        answer.append('L')
        lnow = phone[i]
      elif i in just_right:
        answer.append('R')
        rnow = phone[i]
      else:  
        ld = abs(phone[i][0] - lnow[0]) + abs(phone[i][1] - lnow[1])
        rd = abs(phone[i][0] - rnow[0]) + abs(phone[i][1] - rnow[1])
        
        if ld == rd:
          if hand == "left":
            answer.append('L')
            lnow = phone[i]
          else:
            answer.append('R')
            rnow = phone[i]
        elif min(ld, rd) == ld:
          answer.append('L')
          lnow = phone[i]
        else:
          answer.append('R')
          rnow = phone[i]
    
    return ''.join(answer)
  
numbers = [0, 0, 0, 0]
hand = "right"

result = solution(numbers, hand)
print(result)