def solution(strArr):
    strArr = [len(i) for i in strArr]
    return max([strArr.count(j) for j in set(strArr)])