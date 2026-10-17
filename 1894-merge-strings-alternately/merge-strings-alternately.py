class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word=''
        for i in range(min(len(word1),len(word2))):
            word+=word1[i]+word2[i]
        word+=word1[i+1:]+word2[i+1:]
        return word

        