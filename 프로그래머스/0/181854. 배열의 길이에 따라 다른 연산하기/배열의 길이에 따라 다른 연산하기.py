def solution(arr, n):
    for i in range(-1, -len(arr) - 1, -2):
        arr[i] += n
    return arr