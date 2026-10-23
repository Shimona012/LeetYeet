class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        diff=list()
        for t in timePoints:
            h=int(t[0:2])
            m=int(t[3:])
            diff.append(h*60+m)
        diff.sort()
        ans=1440-diff[-1]+diff[0]
        for i in range(1,len(diff)):
            ans=min(ans,diff[i]-diff[i-1])
        return ans