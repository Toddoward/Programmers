def solution(num_list):
    answer = 0
    while True:
        if len(num_list) == num_list.count(1):
            break
        for i in range(0, len(num_list)):
            if num_list[i] != 1:
                num_list[i] = num_list[i] // 2
                answer += 1
    return answer