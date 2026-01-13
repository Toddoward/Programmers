def solution(numer1, denom1, numer2, denom2):
    common_denom = denom1 * denom2
    sum_numer = (numer1 * denom2) + (numer2 * denom1)

    a = sum_numer
    b = common_denom

    while b:
        a, b = b, a % b

    return [sum_numer // a, common_denom // a]