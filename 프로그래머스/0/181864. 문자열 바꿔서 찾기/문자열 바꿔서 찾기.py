def solution(myString, pat):
    return int(pat in myString.translate(str.maketrans('AB', 'BA')))