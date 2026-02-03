def solution(dots):
    d1, d2, d3, d4 = dots
    
    if ((d2[0] - d1[0]) * (d4[1] - d3[1])) == ((d4[0] - d3[0]) * (d2[1] - d1[1])):
        return 1
    if ((d3[0] - d1[0]) * (d4[1] - d2[1])) == ((d4[0] - d2[0]) * (d3[1] - d1[1])):
        return 1
    if ((d4[0] - d1[0]) * (d3[1] - d2[1])) == ((d3[0] - d2[0]) * (d4[1] - d1[1])):
        return 1
    return 0