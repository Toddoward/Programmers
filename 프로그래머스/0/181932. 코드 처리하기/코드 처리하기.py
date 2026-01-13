def solution(code):
    answer = ''
    mode = False

    for i in range(0, len(code)):
        if code[i] == '1': mode = not mode
        else:
            if not mode and i % 2 == 0:
                answer += code[i]
            elif mode and i % 2 == 1:
                answer += code[i]

    if len(answer) == 0: return 'EMPTY'
    return answer