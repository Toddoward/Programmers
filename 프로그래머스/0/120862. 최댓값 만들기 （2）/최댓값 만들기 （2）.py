def solution(numbers):
    numbers.sort()
    a, b = numbers[0] * numbers[1], numbers[-1] * numbers[-2]
    return max(a, b)