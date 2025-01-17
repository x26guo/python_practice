class Solution:
    def minChanges(self, s: str) -> int:
        l = 0
        r = 1
        swap = 0
        while r < len(s):
            if s[r] != s[l]:
                if r % 2 != 0:
                    swap += 1
                l = r
            r = r + 1


        return swap