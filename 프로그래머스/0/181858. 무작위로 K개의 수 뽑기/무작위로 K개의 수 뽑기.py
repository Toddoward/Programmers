def solution(arr, k):
    arr = list(dict.fromkeys(arr))
    answer = [i for i in arr[:k]]
    return answer + [-1] * (k - len(answer))