def solution(arr):
    while True:
        if bin(len(arr)).count('1') == 1:
            return arr
        arr.append(0)