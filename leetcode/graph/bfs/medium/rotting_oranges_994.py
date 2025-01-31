from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW_SIZE = len(grid)
        COLUMN_SIZE = len(grid[0])
        current_level = []
        next_level = []
        visited = [[False for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]
        fresh_count = 0
        rotten_count = 0

        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_count += 1
                    current_level.append((i,j),)
                    visited[i][j] = True

        if fresh_count == 0: return 0
        if rotten_count == 0: return -1

        minutes = 0
        while current_level:
            cur = current_level.pop()
            row = cur[0]
            column = cur[1]

            # top
            if row - 1 >= 0 and grid[row-1][column] == 1 and not visited[row-1][column]:
                visited[row-1][column] = True
                next_level.append((row-1,column),)
                grid[row-1][column] = 2
                fresh_count -= 1
            # bottom
            if row + 1 < ROW_SIZE and grid[row+1][column] == 1 and not visited[row+1][column]:
                visited[row + 1][column] = True
                next_level.append((row + 1, column), )
                grid[row + 1][column] = 2
                fresh_count -= 1
            # left
            if column - 1 >= 0 and grid[row][column-1] == 1 and not visited[row][column-1]:
                visited[row][column-1] = True
                next_level.append((row, column-1), )
                grid[row][column-1] = 2
                fresh_count -= 1
            # right
            if column + 1 < COLUMN_SIZE and grid[row][column+1] == 1 and not visited[row][column+1]:
                visited[row][column+1] = True
                next_level.append((row, column+1), )
                grid[row][column+1] = 2
                fresh_count -= 1

            if not current_level:
                current_level = next_level[:]
                next_level = []
                minutes += 1


        if fresh_count > 0:
            return -1

        if minutes == 1: return -1
        return minutes - 1


solution = Solution()
grid = [[0,1]]
solution.orangesRotting(grid)