from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW_SIZE = len(grid)
        COLUMN_SIZE = len(grid[0])
        cur_level = []
        next_level = []
        visited = [[False for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]
        connected = [[False for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]

        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                if grid[i][j] == 1:
                    cur_level.append((i,j),)
                    visited[i][j] = True

        while cur_level:
            cur = cur_level.pop()
            row_index = cur[0]
            column_index = cur[1]
            #top
            for i in range(1, ROW_SIZE):
                if row_index - i >= 0  and grid[row_index - i][column_index] == 1:
                    connected[row_index][column_index] = True
                    connected[row_index - i][column_index] = True
                    if not visited[row_index - i][column_index]:
                        next_level.append((row_index - i, column_index),)
                        visited[row_index - i][column_index] = True
                    break

            #bottom
            for i in range(1, ROW_SIZE):
                if row_index + i < ROW_SIZE and grid[row_index + i][column_index] == 1:
                    connected[row_index][column_index] = True
                    connected[row_index + i][column_index] = True
                    if not visited[row_index + i][column_index]:
                        visited[row_index + i][column_index] = True
                        next_level.append((row_index + i, column_index), )
                    break
            #left
            for i in range(1, COLUMN_SIZE):
                if column_index - i >= 0 and grid[row_index][column_index - i] == 1:
                    connected[row_index][column_index] = True
                    connected[row_index][column_index - i] = True
                    if not visited[row_index][column_index - i]:
                        visited[row_index][column_index - i] = True
                        next_level.append((row_index, column_index - i), )
                    break
            #right
            for i in range(1, COLUMN_SIZE):
                if column_index + i < COLUMN_SIZE and grid[row_index][column_index + i] == 1:
                    connected[row_index][column_index] = True
                    connected[row_index][column_index + i] = True
                    if not visited[row_index][column_index + i]:
                        visited[row_index][column_index + i] = True
                        next_level.append((row_index, column_index + i), )
                    break

            if not cur_level:
                cur_level = next_level
                next_level = []

        connected_count = 0
        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                if connected[i][j]:
                    connected_count += 1
        return connected_count

solution = Solution()
grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
solution.countServers(grid)