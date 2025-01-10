from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)
        count = 0
        for word in words:
            if word[:pref_len] == pref:
                count = count + 1
        return count


words = ["pay","attention","practice","attend"]
pref = "at"

solution = Solution()
print(solution.prefixCount(words, pref))