import sys
# sys.stdin = open("C:/Users/JIn/PycharmProjects/coding_Test/input.txt", "rt")

def pretty_print():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end='')
        print()

def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def valid(col, row, val):
    # 가로 축 점검
    for i in range(9):
        if board[col][i] == val:
            return False

    # 세로 축 점검
    for i in range(9):
        if board[i][row] == val:
            return False

    # 3x3 박스 점검
    box_col = col // 3 * 3
    box_row = row // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_col+i][box_row+j] == val:
                return False
    return True

def solution():
    col, row = find_empty()
    if col is None:
        return True
    else:
        for i in range(1, 10):
            if valid(col, row, i):
                board[col][row] = i
                if solution():
                    return True
                board[col][row] = 0
        return False

if __name__ == '__main__':
    board = [list(map(int, input())) for _ in range(9)]
    solution()
    pretty_print()