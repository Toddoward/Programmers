def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, dir_idx = 0, 0, 0

    for i in range(1, n * n + 1):
        answer[x][y] = i
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        
        if not (0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0):
            dir_idx = (dir_idx + 1) % 4
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        
        x, y = nx, ny
        
    return answer