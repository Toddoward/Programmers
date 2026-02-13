def solution(A, B):
    if A == B: return 0
    for i in range(1, len(A)):
        if A[len(A) - i:len(A)] + A[0:len(A) - i] == B:
            return i
    return -1