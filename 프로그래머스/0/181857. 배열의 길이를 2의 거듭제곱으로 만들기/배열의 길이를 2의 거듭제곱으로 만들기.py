def solution(arr):
    if bin(len(arr)).count('1') == 1:
        return arr
    while True:
        arr.append(0)
        if bin(len(arr)).count('1') == 1:
            return arr