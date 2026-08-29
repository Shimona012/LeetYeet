class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers=list()
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i+j==target:
                    numbers=[nums.index(i),nums.index(j,nums.index(i)+1)]
                    break
        return numbers
        