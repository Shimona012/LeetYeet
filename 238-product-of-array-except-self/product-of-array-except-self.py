class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #answer=[]
        answer=[1]*len(nums)
        #prefix=[1]
        #suffix=[1]*len(nums)
        for i in range(1,len(nums)):
            #prod=prefix[i-1]*nums[i-1]
            #prefix.append(prod)
            answer[i]=answer[i-1]*nums[i-1]
        #for j in range(len(nums)-2,-1,-1):
        #    suffix[j]=suffix[j+1]*nums[j+1]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        #for k in range(len(nums)):
        #    answer.append(prefix[k]*suffix[k])
        return answer