def solution(before, after):
    return int([after.count(c) for c in set(before)] == [before.count(c) for c in set(before)]) if set(after) == set(before) else 0