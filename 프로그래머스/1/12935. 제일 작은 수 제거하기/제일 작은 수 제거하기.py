def solution(arr):
    arr.remove(min(arr))
    return arr if bool(len(arr)) else [-1]