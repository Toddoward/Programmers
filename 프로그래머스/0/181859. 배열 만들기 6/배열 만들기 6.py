def solution(arr):
    if not arr: return [-1]
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
            
    return answer if answer else [-1]