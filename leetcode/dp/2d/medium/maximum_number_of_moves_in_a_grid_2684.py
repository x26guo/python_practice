from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROW_SIZE = len(grid)
        COLUMN_SIZE = len(grid[0])
        dp = [[0 for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]

        for i in range(ROW_SIZE):
            dp[i][COLUMN_SIZE - 1] = 0

        for column_index in range(COLUMN_SIZE - 2, -1, -1):
            for row_index in range(ROW_SIZE - 1, -1, -1):
                cur = grid[row_index][column_index]
                ## compare upper right
                if row_index - 1 >= 0 and column_index + 1 < COLUMN_SIZE and grid[row_index - 1][column_index + 1] > grid[row_index][column_index]:
                    dp[row_index][column_index] = max(dp[row_index][column_index], dp[row_index - 1][column_index + 1] + 1)
                ## compare right
                if column_index + 1 < COLUMN_SIZE and grid[row_index][column_index + 1] > grid[row_index][column_index]:
                    dp[row_index][column_index] = max(dp[row_index][column_index], dp[row_index][column_index + 1] + 1)
                ## compare bottom right
                if row_index + 1 < ROW_SIZE and column_index + 1 < COLUMN_SIZE and grid[row_index + 1][column_index + 1] > grid[row_index][column_index]:
                    dp[row_index][column_index] = max(dp[row_index][column_index], dp[row_index + 1][column_index + 1] + 1)

        max_steps = 0
        for i in range(ROW_SIZE):
            if dp[i][0] > max_steps:
                max_steps = dp[i][0]
        return max_steps