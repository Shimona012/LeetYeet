class Solution(object):
    def isMonotonic(self, nums):
        """:type nums: List[int]:rtype: bool"""
        sorted_nums=sorted(nums)
        if sorted_nums==nums or sorted_nums[::-1]==nums:
            return True
        else:
            return False