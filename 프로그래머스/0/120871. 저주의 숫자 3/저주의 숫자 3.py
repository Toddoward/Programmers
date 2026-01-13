def solution(n):
    answer = 0
    max_step = n

    while (answer < max_step):
        if (answer + 1) % 3 == 0 or '3' in str(answer + 1):
            max_step += 1
        answer += 1 
    return answer