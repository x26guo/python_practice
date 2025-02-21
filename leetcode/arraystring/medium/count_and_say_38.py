class Solution:
    def countAndSay(self, n: int) -> str:


        def helper(s : str):
            output = ''
            slow = 0
            fast = 0

            while fast < len(s):
                if s[fast] == s[slow]:
                    fast += 1
                else:
                    count = fast - slow
                    output += str(count) + str(s[slow])
                    slow = fast

            count = fast - slow
            output += str(count) + str(s[slow])
            return output

        if n == 1:
            return "1"
        s = "1"
        for i in range(1, n):
            s = helper(s)
        return s

solution = Solution()
solution.countAndSay(4)

