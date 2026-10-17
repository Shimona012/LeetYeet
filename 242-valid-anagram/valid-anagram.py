class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_s=set(list(s))
        letter_t=set(list(t))
        if len(letter_t)!=len(letter_s):
            return False
        else:
            for i in list(letter_s):
                if t.count(i)!=s.count(i):
                    return False
            else:
                return True


        