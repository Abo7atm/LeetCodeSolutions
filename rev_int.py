# https://leetcode.com/problems/reverse-integer/
# Passed: 32ms, 13.7MB

def reverse(x: int) -> int:
    return int(str(x)[::-1]) if str(x)[0] !='-' else int('-'+str(x)[:0:-1])


if __name__ == '__main__':
    print('{} -> {}'.format(123, reverse(123)))
    print('{} -> {}'.format(-123, reverse(-123)))
    print('{} -> {}'.format(101, reverse(101)))
    print('{} -> {}'.format(123, reverse(123)))
