def solution(numlist, n):
    return [i[1] for i in sorted([(abs(num - n), num) for num in numlist], key=lambda x: (x[0], -x[1]))]