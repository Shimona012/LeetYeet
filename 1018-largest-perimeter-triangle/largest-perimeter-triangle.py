class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            sides=nums[i:i+3]
            if sides[0]<sides[1]+sides[2]:
                return sum(sides)
        return 0