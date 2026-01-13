def solution(s):
    sl = s.split(' ')
    sl = [i.capitalize() for i in sl]
    answer = ' '.join(sl)
    return answer