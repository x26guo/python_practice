class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0

        max_length = 0
        cur_cost = 0
        for r in range(len(s)):
            cur_cost += abs(ord(s[r]) - ord(t[r]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            max_length = max(r - l + 1, max_length)

        return max_length

