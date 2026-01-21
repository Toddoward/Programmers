def solution(my_str, n):
    amount = len(my_str) // n if len(my_str) % n == 0 else (len(my_str) // n) + 1
    return [my_str[i*n:i*n + n] for i in range(amount)]