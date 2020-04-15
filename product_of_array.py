# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/

def product(nums):
    s = len(nums)
    a = [1] * s
    b = [1] * s
    for i in range(s-1):
        j = s - i - 1
        a[i+1] = nums[i] * a[i]
        b[j-1] = nums[j] * b[j]

    return [i*j for i,j in zip(a,b)]

if __name__ == '__main__':
    r = product([1,2,3,4])
    assert r == [24,12,8,6], '{} should be [24, 12, 8, 6]'.format(r)
