from test_framework import generic_test

def add(a, b):
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def multiply(x: int, y: int) -> int:
    res = 0
    while x:
        if x & 1:
            res = add(res, y)
        x >>= 1
        y <<= 1
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
