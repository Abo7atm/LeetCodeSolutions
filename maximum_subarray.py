# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/

def max_subarray(nums):
    first = nums[0]
    if len(nums) == 1: print(first); return first
    g = first
    c = first 
    for i in nums[1:]:
        c = max(i, c+i)
        g = max(c, g)
    print(g)
    return g

if __name__ == '__main__':
    test_list = [-2,1,-3,4,-1,2,1,-5,4]
    assert max_subarray(test_list) == 6
    assert max_subarray([-1]) == -1, 'should be equal to -1'
    assert max_subarray([-2, 1]) == 1
    assert max_subarray([-2, -1]) == -1
    assert max_subarray([-1, -2]) == -1
