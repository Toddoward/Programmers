def solution(n):
    return [[1 if k == i else 0 for i in range(n)] for k in range(n)]