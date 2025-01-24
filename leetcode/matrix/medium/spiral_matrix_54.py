from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW_SIZE = len(matrix)
        COLUMN_SIZE = len(matrix[0])
        count = ROW_SIZE * COLUMN_SIZE
        visited = [[False for x in range(COLUMN_SIZE)] for y in range(ROW_SIZE)]
        row_index = 0
        column_index = 0
        output = []
        while count > 0:

            # go right
            while column_index < COLUMN_SIZE and not visited[row_index][column_index]:
                output.append(matrix[row_index][column_index])
                visited[row_index][column_index] = True
                count -= 1
                column_index += 1
            column_index -= 1
            row_index += 1

            # go bottom
            while row_index < ROW_SIZE and not visited[row_index][column_index]:
                output.append(matrix[row_index][column_index])
                visited[row_index][column_index] = True
                count -= 1
                row_index += 1
            row_index -=1
            column_index -=1

            # go left
            while column_index >= 0 and not visited[row_index][column_index]:
                output.append(matrix[row_index][column_index])
                visited[row_index][column_index] = True
                count -= 1
                column_index -= 1
            column_index += 1
            row_index -= 1

            # go up
            while row_index >= 0 and not visited[row_index][column_index]:
                output.append(matrix[row_index][column_index])
                visited[row_index][column_index] = True
                count -= 1
                row_index -= 1
            row_index +=1
            column_index += 1
        return output

solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.spiralOrder(matrix)