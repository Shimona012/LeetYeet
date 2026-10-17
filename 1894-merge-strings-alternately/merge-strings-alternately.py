class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1,n2=len(word1),len(word2)
        n=min(n1,n2)
        word=list()
        for i in range(n):
            word.append(word1[i])
            word.append(word2[i])
        word.append(word1[n:])
        word.append(word2[n:])
        word="".join(word)
        return word

        