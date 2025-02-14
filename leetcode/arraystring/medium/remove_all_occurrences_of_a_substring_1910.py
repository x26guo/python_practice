class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            s = s.replace(part, "", 1)
        return s

solution = Solution()
s = "daabcbaabcbc"
part = "abc"
solution.removeOccurrences(s, part)