def solution(board, moves):
    answer = 0
    
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                item = board[j][i-1]
                board[j][i-1] = 0
                if len(stack) != 0:
                    if stack[-1] == item:
                        answer += 2
                        stack.pop()
                    else:
                        stack.append(item)
                else:
                    stack.append(item)
                break
    
    return answer
  
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

result = solution(board, moves)
print(result)