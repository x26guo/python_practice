class Solution:
    def minimumLength(self, s: str) -> int:
        dic = {}
        total_len = 0;
        for str in s:
            if str in dic:
                dic[str] = dic[str] + 1
                if dic[str] >= 3:
                    dic[k] = dic[k] - 2
                    total_len = total_len - 2
            else:
                dic[str] = 1
            total_len = total_len + 1

        return total_len