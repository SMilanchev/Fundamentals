end_num = int(input())

for i in range(1, end_num + 1):
    sum_digits = 0
    for digit in str(i):
        sum_digits = sum_digits + int(digit)

        is_special = sum_digits == 5 or sum_digits == 7 or sum_digits == 11

    print(f"{i} -> {is_special}")