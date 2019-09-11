def rotate(nums, k):
    nums = nums[len(nums)-k:]+nums[:-k]
    return nums


if __name__=='__main__':
    print(rotate([1], 0), end='')
    print(' must be [1]')
    print(rotate(list(range(1, 8)), 3), end='')
    print(' must be [5,6,7,1,2,3,4]')
