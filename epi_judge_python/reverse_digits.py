from test_framework import generic_test


def reverse(x: int) -> int:
    sign = 1
    res = 0
    if x < 0:
        sign = -1
        x = abs(x)
    while x:
        last_digit = x % 10
        res *= 10
        res += last_digit
        x //= 10
    return sign * res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
