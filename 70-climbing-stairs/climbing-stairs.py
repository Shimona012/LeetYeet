class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        steps=0
        for k in range(n//2+1):
            steps+=math.comb(n - k, k)
        return steps