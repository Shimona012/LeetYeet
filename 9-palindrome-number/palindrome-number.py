class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        #With sting
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
        #Without string
        num=0
        og=x
        while x>0:
            num=(10*num+x%10)
            x//=10
        if og==num:
            return True
        else:
            return False
        
        


        