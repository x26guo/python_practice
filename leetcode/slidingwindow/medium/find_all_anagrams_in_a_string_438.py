from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        dic_p = {}
        dic_s = {}
        for i in range(len(p)):
            dic_p[p[i]] = dic_p.get(p[i], 0) + 1
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1

        output = []
        if dic_p == dic_s:
            output.append(0)

        l = 0
        for i in range(len(p), len(s)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1
            dic_s[s[l]] = dic_s[s[l]] - 1
            if dic_s[s[l]] == 0:
                dic_s.pop(s[l])
            l+=1
            if dic_p == dic_s:
                output.append(l)
        return output