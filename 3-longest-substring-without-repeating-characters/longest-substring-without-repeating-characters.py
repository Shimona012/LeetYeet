class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        poss,taken,inuse=set(),set(),str()
        for i in s:
            if i in taken:
                poss.add(inuse)
                while i in taken:
                    taken.remove(inuse[0])
                    inuse=inuse[1:]
            taken.add(i)
            inuse+=i
        return max(len(inuse),max(map(len,poss),default=0))