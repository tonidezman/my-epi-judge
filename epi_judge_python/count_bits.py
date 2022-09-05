from test_framework import generic_test


def count_bits(x: int) -> int:
    res = 0
    while x:
        if x & 1:
            res += 1
        x >>=1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
