def solution(board, k):
    n = len(board)
    m = len(board[0])
    
    return sum(board[i][j] 
               for i in range(min(k + 1, n)) 
               for j in range(min(k - i + 1, m)))