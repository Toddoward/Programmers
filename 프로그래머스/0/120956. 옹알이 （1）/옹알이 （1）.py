def solution(babbling):
    pron = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        b_t = b
        for p in pron:
            b_t = b_t.replace(p, '*' * len(p))
        if b_t == "*" * len(b):
            answer += 1
    return answer