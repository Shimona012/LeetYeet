class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=dict()
        length=0
        for i in s:
            count[i] = count.get(i, 0) + 1
        for f in count.values():
            length+=(f//2) * 2
        if length<len(s):
            length+= 1
        return length
                
            