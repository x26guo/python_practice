from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW_SIZE = len(isWater)
        COLUMN_SIZE = len(isWater[0])
        cur_level = []
        next_level = []
        visited = [[False for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]
        output = [[-1 for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]

        #step 1: find water and add 0 to output
        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    cur_level.append((i,j),)
                    visited[i][j] = True
        val = 0
        while cur_level:
            cur = cur_level.pop()
            row_index = cur[0]
            column_index = cur[1]
            visited[row_index][column_index] = True
            output[row_index][column_index] = val

            # check top
            if row_index - 1 >= 0 and not visited[row_index - 1][column_index]:
                next_level.append((row_index - 1, column_index), )
                visited[row_index - 1][column_index] = True

            # check bottom
            if row_index + 1 < ROW_SIZE and not visited[row_index + 1][column_index]:
                next_level.append((row_index + 1, column_index), )
                visited[row_index + 1][column_index] = True

            # check left
            if column_index - 1 >= 0 and not visited[row_index][column_index - 1]:
                next_level.append((row_index, column_index - 1), )
                visited[row_index][column_index - 1] = True

            # check right
            if column_index + 1 < COLUMN_SIZE and not visited[row_index][column_index + 1]:
                next_level.append((row_index, column_index + 1), )
                visited[row_index][column_index + 1] = True

            if not cur_level:
                val += 1
                cur_level = next_level
                next_level = []

        return output

solution = Solution()
solution.highestPeak([[0,0,1],[1,0,0],[0,0,0]])