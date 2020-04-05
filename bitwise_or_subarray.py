# https://leetcode.com/problems/bitwise-ors-of-subarrays/
from functools import reduce

def subarray_bitwise_or(a):
    subs = [[]]
    res = []
    bitwise_or = lambda x,y: x|y
    for i in range(len(a)):
        n = i + 1
        while n <= len(a):
            sub = a[i:n]
            subs.append(sub)
            res.append(reduce(bitwise_or, sub))
            n += 1

    return len(set(res))

if __name__=='__main__':
    assert subarray_bitwise_or([0]) == 1
    assert subarray_bitwise_or([1,1,2]) == 3
    assert subarray_bitwise_or([1,2,4]) == 6
