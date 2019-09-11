# https://leetcode.com/problems/find-pivot-index/


def pivot_index(nums):
    # Rough draft
    right = left = mid = 0
    """ Sum of the elements on the right of the current element
    should be equal to the sum of the elements on the left
    """
    nums = list(nums)
    for i,v in enumerate(nums):
        if i == 0:
            left = 0
            right = [i+1:]
        else:
            left = sum(nums[:i+1])
            middle = nums[i+1]
            if i+2 == len(nums):
                break
            right = sum(nums[i+2:])

        print('
        if right == left:
            return i+1
    return -1

if __name__=='__main__':
    # print(pivot_index([1, 7, 3, 6, 5, 6]))
    # print(pivot_index([1,2,3]))
    print(pivot_index([-1,-1,-1,-1,0,1]))


