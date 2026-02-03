def solution(arr):
    if len(arr) > len(arr[0]):
        d = len(arr) - len(arr[0])
        for i in arr:
            i.extend([0] * d)
    elif len(arr) < len(arr[0]):
        d = len(arr[0]) - len(arr)
        for _ in range(d):
            arr.append([0] * len(arr[0]))
    return arr