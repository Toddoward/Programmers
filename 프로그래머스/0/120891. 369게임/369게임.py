def solution(order):
    return len([c for c in str(order) if c in '369'])