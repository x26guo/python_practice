class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1: return 1
        pre = 1
        current = pre
        for i in range(2, n + 1):
            current = pre + (i - 1) * 4
            pre = current
        return current

solution = Solution()
solution.coloredCells(2)