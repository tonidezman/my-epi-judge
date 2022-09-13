from test_framework import generic_test

def get_weight(x):
    res = 0
    while x:
        x = x & (x - 1)
        res += 1
    return res

def closest_int_same_bit_count(x: int) -> int:
    weight_x = get_weight(x)
    curr_neg = x - 1
    curr_pos = x + 1
    while True:
        if get_weight(curr_neg) == weight_x:
            return curr_neg
        if get_weight(curr_pos) == weight_x:
            return curr_pos
        curr_neg -= 1
        curr_pos += 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
