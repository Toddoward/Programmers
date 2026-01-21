def solution(n):
    res, base = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    n_temp = n - 1 if n > 0 else 0
    while n_temp > 0:
        if n_temp % 2 == 1:
            res = [[sum(res[i][k] * base[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        base = [[sum(base[i][k] * base[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        n_temp //= 2
    return res[0][0] % 1234567 if n > 0 else 0
