from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # select an element ...
    for i,v in enumerate(nums):
        # if element is greater than the target, skip
        if v > target:
            pass
        # ... then iterate through the list to find other element
        # that make pair equal target
        for j,b in enumerate(nums[i+1:]):
            print({'i': i, 'v': v, 'j': j, 'b': b})
            # if element is greater than the target, skip
            if b > target:
                pass
            # return if pair equal target
            if v+b == target:
                print('DONE')
                # how to fix same element selection?
                # return [nums.index(v), nums.index(b)]
                return [i, j+i+1]
    return [0,0]

if __name__ == '__main__':
    # first test
    nums = [2, 7, 11, 15]
    print(two_sum(nums, 9))
    assert two_sum(nums, 9) == [0,1]

    # second test
    nums = [3, 2, 4]
    print(two_sum(nums, 6))
    assert two_sum(nums, 6) == [1,2]

    # third test
    nums = [3, 3]
    print(two_sum(nums, 6))
    assert two_sum(nums, 6) == [0,1]
