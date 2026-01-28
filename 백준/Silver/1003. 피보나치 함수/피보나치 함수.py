import sys
input = sys.stdin.readline

N = int(input())
lines = [int(input().strip()) for _ in range(N)]

for n_val in lines:
    if n_val == 0:
        print(1, 0)
        continue
    
    res, base = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    temp = n_val
    while temp > 0:
        if temp % 2 == 1:
            
            res = [[sum(res[r][k] * base[k][j] for k in range(2)) for j in range(2)] for r in range(2)]
        base = [[sum(base[r][k] * base[k][j] for k in range(2)) for j in range(2)] for r in range(2)]
        temp //= 2
    
    print(res[1][1], res[0][1])