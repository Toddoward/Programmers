def solution(absolutes, signs):
    return sum([absolutes[i] for i in range(0, len(signs)) if signs[i]])\
            - sum([absolutes[i] for i in range(0, len(signs)) if not signs[i]])