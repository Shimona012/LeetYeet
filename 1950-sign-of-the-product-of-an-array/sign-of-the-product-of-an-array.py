class Solution(object):
    def arraySign(self, nums):
        """:type nums: List[int]:rtype: int"""
        def signFunc(x):
            if x > 0: return 1
            if x < 0: return -1
            return 0
        product = 1
        for num in nums:
            product *= num
        return signFunc(product)
        