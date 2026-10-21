class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        start=1
        while len(word)<=k:
            word += ''.join(chr((ord(c) - 96) % 26 + 97) for c in word[:start])
            start *= 2
        return word[k - 1]