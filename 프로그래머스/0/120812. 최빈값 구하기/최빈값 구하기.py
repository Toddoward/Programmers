def solution(array):
    count = [array.count(i) for i in array]
    if (count.count(max(count)) == array.count(array[count.index(max(count))])):
        return array[count.index(max(count))]
    return -1