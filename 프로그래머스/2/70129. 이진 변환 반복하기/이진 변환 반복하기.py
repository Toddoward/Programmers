def solution(s):
    count = 0
    zero = 0

    while len(s) > 1:
        len_s = len(s)
        s = s.replace("0", "")
        zero += len_s - len(s)
        s = bin(int(len(s))).replace("0b", "")
        count += 1

    return [count, zero]