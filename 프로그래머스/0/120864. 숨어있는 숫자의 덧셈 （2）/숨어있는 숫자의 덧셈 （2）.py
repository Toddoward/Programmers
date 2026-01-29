def solution(my_string):
    my_str = list(my_string)
    for i in range(len(my_str)):
        if not my_str[i].isdecimal():
            my_str[i] = ' '
    my_str = ''.join(my_str)
    return sum([int(j) for j in my_str.split() if j])