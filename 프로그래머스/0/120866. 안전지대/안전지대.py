def solution(board):
    n = len(board)
    danger_zone = set()

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < n and 0 <= j < n:
                            danger_zone.add((i, j))
    
    return n**2 - len(danger_zone)