from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        column_size = len(grid[0])
        prefix_row1, prefix_row2 = [0] * column_size, [0] * column_size
        prefix_row1[0] = grid[0][0]
        prefix_row2[0] = grid[1][0]

        for i in range(1,column_size):
            prefix_row1[i] = prefix_row1[i - 1] + grid[0][i]
            prefix_row2[i] = prefix_row2[i - 1] + grid[1][i]

        res = float("inf")
        for i in range(column_size):
            top = prefix_row1[column_size - 1] - prefix_row1[i]
            bottom = prefix_row2[i - 1] if i > 0 else 0
            second_robot = max(top, bottom)
            res = min(res, second_robot)

        return res