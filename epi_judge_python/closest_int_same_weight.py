from test_framework import generic_test

def swap_bits(x, i, j):
    mask = (1 << i) | (1 << j)
    return x ^ mask

def closest_int_same_bit_count(x: int) -> int:
    i, j = 0, 1
    while True:
        if ((x >> i) & 1) ^ ((x >> j) & 1):
            return swap_bits(x, i, j)
        i += 1
        j += 1




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
