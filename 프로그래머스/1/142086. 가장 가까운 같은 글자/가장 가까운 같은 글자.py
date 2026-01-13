def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        n = 1
        found = False
        for j in range(i - 1, -1, -1):
            if s[j] == s[i]:
                found = True
                break
            n += 1
        if not found:
            answer.append(-1)
        else:
            answer.append(n)
    return answer