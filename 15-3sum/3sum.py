class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        num=set()
        for i in range(n-2):
            num_in=set()
            for j in range(i+1,n):
                need=-(nums[i]+nums[j])
                if need in num_in:
                    pair=(nums[i],need,nums[j])
                    num.add(pair)
                num_in.add(nums[j])
        num=[list(x) for x in num]
        
        '''
            if nums[i]==nums[i+1] and nums[i]==nums[i+2] and nums[i+1]==nums[i+2]:
                continue
            else:
                if nums[i]+nums[i+1]+nums[i+2]==0:
                    num.append([nums[i],nums[i+1],nums[i+2]])
        for j in num:
            j.sort()
        num=list(set(tuple(x) for x in num))
        return num'''
    
        '''for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i!=j and i!=k and j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            num.append(tuple(sorted(list((nums[i],nums[j],nums[k])))))
        
        num=list(set(num))
        #lacks complexity efficiency'''

        return num
        