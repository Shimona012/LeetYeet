import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        app_pow=round(math.log(n,4))
        return 4**app_pow==n
        