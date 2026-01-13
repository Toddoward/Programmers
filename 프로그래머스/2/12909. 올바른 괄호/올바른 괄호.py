def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False

    i = 0
    j = 0

    for k in range(0, len(s)):
        if s[k] == '(':
            i += 1
        else:
            j += 1

        if j > i:
            return False
    
    if i != j:
        return False

    return True