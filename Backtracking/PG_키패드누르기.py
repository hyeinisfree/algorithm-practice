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
        ld = bfs(lnow, phone[i])
        rd = bfs(rnow, phone[i])
        
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
    
def bfs(start, end):  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  queue = deque()
  queue.append(start)
  
  graph = [[1] * 3 for _ in range(4)]
  while queue:
    x, y = queue.popleft()
    
    if x == end[0] and y == end[1]:
        return graph[x][y] - 1
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= 4 or ny >= 3:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
numbers = [0, 0, 0, 0]
hand = "right"

result = solution(numbers, hand)
print(result)