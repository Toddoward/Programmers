def solution(polynomial):
    polynomial = polynomial.split(' + ')
    nums = [i for i in polynomial if 'x' not in i]
    x = sum([int(j.replace('x', '') or '1') for j in polynomial if j not in nums])
    n = sum([int(k) for k in nums])
    
    answer = []
    if x:
        answer.append('x' if x == 1 else f'{x}x')
    if n:
        answer.append(f'{n}')
    return ' + '.join(answer)