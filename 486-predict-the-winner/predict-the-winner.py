class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def predict(l, r):
            if l==r:
                return nums[l]
            return max(nums[l]-predict(l+1,r),nums[r] -predict(l,r-1))
        return predict(0, len(nums)-1)>=0