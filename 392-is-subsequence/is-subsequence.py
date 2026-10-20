class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s,t,i=list(s),list(t),0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)