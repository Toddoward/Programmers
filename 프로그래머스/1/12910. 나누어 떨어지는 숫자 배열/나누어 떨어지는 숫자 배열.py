def solution(arr, divisor):
    n = [i for i in arr if i % divisor == 0]
    return sorted(n) if len(n) != 0 else [-1] 