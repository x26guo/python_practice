class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        dic = {}
        count = 0
        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]] = dic[s[r]] + 1
            else:
                dic[s[r]] = 1
            while "a" in dic and "b" in dic and "c" in dic:
                count += (len(s) - r)
                dic[s[l]] = dic[s[l]] - 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l +=1
        return count