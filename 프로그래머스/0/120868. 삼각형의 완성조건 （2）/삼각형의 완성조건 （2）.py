def solution(sides):
    return len([i for i in range(max(sides) - min(sides) + 1, sum(sides)) if max(sides) < min(sides) + i or i < sum(sides) ])