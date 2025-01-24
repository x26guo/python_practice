class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        slow = 0
        res = 0
        for fast in range(len(s)):
            if s[fast] in store:
                store[s[fast]] = store[s[fast]] + 1
            else:
                store[s[fast]] = 1

            max_value = max(store.values())
            while (fast - slow + 1) - max_value > k:
                store[s[slow]] = store[s[slow]] - 1
                slow += 1

            res = max(res, fast - slow + 1)
        return res




solution = Solution()
s = "AABABBA"
k = 1
solution.characterReplacement(s,k)