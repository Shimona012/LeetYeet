class Solution:
    def mySqrt(self, x: int) -> int:
        n=x//2
        num=0
        if x<2:
            return x
        for i in range(n + 1):
            if i*i<=x:
                num=i
            else:
                break

        return num
        