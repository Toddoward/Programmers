def solution(a, b, c, d):
    if len({a, b, c, d}) == 4:
        return min([a, b, c, d])
    dice = f'{a}{b}{c}{d}'
    for i in range(1, 7):
        if str(i) in dice:
            if dice.count(str(i)) == 4:
                return int(dice)
            elif dice.count(str(i)) == 3:
                return (10 * i + int(dice.replace(str(i), ''))) ** 2
            elif dice.count(str(i)) == 2:
                rest = dice.replace(str(i), '')
                if rest[0] == rest[1]:
                    return (i + int(rest[0])) * abs(i - int(rest[0]))
                else:
                    return int(rest[0]) * int(rest[1])