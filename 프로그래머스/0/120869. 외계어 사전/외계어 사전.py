def solution(spell, dic):
    answer = 2
    counter = 0

    for word in dic:
        if set(spell).issubset(set(word)):
            counter += 1
        if counter > 1:
            return 2
    if counter == 1:
        return 1

    return answer