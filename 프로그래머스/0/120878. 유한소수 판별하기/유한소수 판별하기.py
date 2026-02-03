def solution(a, b):
    divisor = 1
    for i in range(max(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            divisor = i
            break
    
    
    divisors = [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 512, 625, 640, 800, 1000]
    
    return 1 if b//divisor in divisors else 2