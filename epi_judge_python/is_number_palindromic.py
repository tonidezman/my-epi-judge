from test_framework import generic_test

from math import floor, log10

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_of_digits = floor(log10(x)) + 1
    msd_mask = 10**(num_of_digits - 1)
    for i in range(num_of_digits // 2):
        lsd = x % 10
        msd = x // msd_mask
        if msd != lsd:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
