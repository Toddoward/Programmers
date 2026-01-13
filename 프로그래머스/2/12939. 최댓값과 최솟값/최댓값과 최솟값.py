def solution(s):
    s_l = s.split(' ')
    s_l = [int(i) for i in s_l]
    s_l.sort()
    return f'{s_l[0]} {s_l[-1]}'