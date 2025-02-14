class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0: return 0
        open_count = 0
        additional_close_count = 0
        for c in s:
            if c == '(':
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    additional_close_count += 1
                    open_count = 0
        return open_count + additional_close_count