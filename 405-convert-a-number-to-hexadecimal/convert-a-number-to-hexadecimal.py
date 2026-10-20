class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits="0123456789abcdef"
        num&=0xFFFFFFFF
        hex_code=str()
        while num:
            hex_code+=digits[num % 16]
            num //= 16
        return hex_code[::-1]
            