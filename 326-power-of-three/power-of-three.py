import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        app_pow=round(math.log(n,3))
        return 3**app_pow==n
        