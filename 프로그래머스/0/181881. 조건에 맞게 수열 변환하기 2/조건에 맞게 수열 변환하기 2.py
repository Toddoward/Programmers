def solution(arr):
    answer = 0
    is_changed = False
    while True:
        is_changed = False
        for i in range(0, len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                is_changed = True
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
                is_changed = True
        if is_changed:
            answer += 1
        else:
            break
    return answer