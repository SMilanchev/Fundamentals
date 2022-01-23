def range_from_centre(a, b):
    return a * a + b * b


def solve(a, b, c, d):
    point_one = range_from_centre(a, b)
    point_two = range_from_centre(c, d)

    if point_one > point_two:
        print((int(c), int(d)))
    else:
        print((int(a), int(b)))


a = float(input())
b = float(input())
c = float(input())
d = float(input())

solve(a, b, c, d)