class Solution:
    def maxValue(self, n: str, x: int) -> str:
        positive = True

        if n[0] == '-': positive = False

        if positive:
            for i in range(len(n)):
                if int(n[i]) < x:
                    if i == 0:
                        return str(x) + n
                    else:
                        return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    if i == 1:
                        return "-" + str(x) + n[1:]
                    else:
                        return n[:i] + str(x) + n[i:]
            return n + str(x)

solution = Solution()
n = "-13"
x = 2
solution.maxValue(n, x)