def solution(quiz):
    answer = []
    for i in quiz:
        q, a = i.split(' = ')
        q = q.split()
        if q[1] == '+' and int(q[0]) + int(q[2]) == int(a):
            answer.append('O')
        elif q[1] == '-' and int(q[0]) - int(q[2]) == int(a):
            answer.append('O')
        else: answer.append('X')
    return answer