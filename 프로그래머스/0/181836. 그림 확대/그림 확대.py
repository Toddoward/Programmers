def solution(picture, k):
    return [line for row in picture for line in [''.join([charecter * k for charecter in row])] * k]