import sys
input = sys.stdin.readline

def mul(A, B):
    return [[sum(a * b for a, b in zip(ra, cb)) for cb in zip(*B)] for ra in A]

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    
    res, base = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    while n > 0:
        if n % 2:
            res = mul(res, base)
        base = mul(base, base)
        n //= 2
    
    print(res[1][1], res[0][1])