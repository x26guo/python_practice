class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1

        output = ""
        for k,v in sorted(dic.items(), key = lambda x: -x[1]):
            output += str(k * v)
        return output

solution = Solution()
s = "tree"
solution.frequencySort(s)