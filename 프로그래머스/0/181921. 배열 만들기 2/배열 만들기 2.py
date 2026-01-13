def solution(l, r):
    answer = [i for i in range(l, r + 1) if str(i).count("0") + str(i).count("5") == len(str(i))]
    if len(answer) == 0: return [-1]
    return answer