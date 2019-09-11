# https://leetcode.com/problems/remove-element/
# 20ms, 11.6MB

def removeElement(self, nums, val):
    for i in range(2):
        for i,v in enumerate(nums):
            if v == val:
                nums.pop(i)
    return len(nums)   