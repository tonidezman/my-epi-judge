from test_framework import generic_test

def get_bit(x, i):
    return (x >> i) & 1

def swap(x, i, j):
    mask = (1 << i) | (1 << j)
    return x ^ mask

def swap_bits(x, i, j):
    if get_bit(x, i) == get_bit(x, j):
        return x
    return swap(x, i, j)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
