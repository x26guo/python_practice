from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0]) - 1
        val = matrix[row][column]

        while True:
            if target == val:
                return True
            elif target > val:
                row += 1
                if row > len(matrix) - 1:
                    return False
            else:
                column -= 1
                if column < 0:
                    return False
            val = matrix[row][column]