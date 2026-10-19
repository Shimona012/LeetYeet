class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack:
                    top_element=stack.pop()
                else:
                    top_element='NA'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack