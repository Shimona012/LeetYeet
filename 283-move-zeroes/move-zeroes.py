class Solution(object):
    def moveZeroes(self, nums):
        """:type nums: List[int]:rtype: None Do not return anything, modify nums in-place instead."""
        nums[:] = [x for x in nums if x != 0] + [0] * nums.count(0)
        return nums
        