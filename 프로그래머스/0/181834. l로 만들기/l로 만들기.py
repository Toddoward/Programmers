def solution(myString):
    return ''.join(['l' if c in 'abcdefghijk' else c for c in myString])