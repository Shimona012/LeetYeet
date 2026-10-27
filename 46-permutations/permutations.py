import random
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms=set()
        pnr=1
        for i in range(1,len(nums)+1):
            pnr*=i    
        while len(perms)!=pnr:
                p=tuple(random.sample(nums,len(nums)))
                perms.add(p)
        return [list(p) for p in perms]