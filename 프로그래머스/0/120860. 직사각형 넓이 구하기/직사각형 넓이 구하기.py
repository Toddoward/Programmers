def solution(dots):
    for i in range(1, len(dots)):
        if dots[0][0] != dots[i][0] and dots[0][1] != dots[i][1]:
            return abs((dots[0][0] - dots[i][0]) * (dots[0][1] - dots[i][1]))