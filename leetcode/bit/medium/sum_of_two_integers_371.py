class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0Xffffffff
        while mask & b > 0:
            x = a ^ b
            y = (a & b) << 1
            a = x
            b = y
        if b > 0:
            return mask & a
        else:
            return a