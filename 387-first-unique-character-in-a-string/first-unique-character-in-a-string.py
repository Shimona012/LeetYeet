from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        od=OrderedDict()
        for i,ch in enumerate(s):
            if ch not in od:
                od[ch]=[1,i]
            else:
                od[ch][0]+=1
        for ch,(count,index) in od.items():
            if count==1:
                return index
        return -1