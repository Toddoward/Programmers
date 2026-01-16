def solution(array, n):
    array.sort()
    min_diff = float('inf')
    answer = 0
    
    for i in array:
        if abs(n - i) < min_diff:
            min_diff = abs(n - i)
            answer = i
            
    return answer