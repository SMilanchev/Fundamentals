def is_positive(a, b, c):
    return a > 0 and b > 0 and c > 0


def is_negative(a, b, c):
    return (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0) or \
           (a > 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c < 0)


def is_zero(a, b, c):
    return a == 0 or b == 0 or c == 0


def solve(a, b, c):
    cases = [
        [is_negative, "negative"],
        [is_positive, "positive"],
        [is_zero, "zero"]
    ]
    for fn, case in cases:
        if fn(a, b, c):
            print(case)


a = int(input())
b = int(input())
c = int(input())
solve(a, b, c)