from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        columns = len(board[0])
        visited = [[False for x in range(columns)] for y in range(rows)]

        def convert_to_T(row_index, column_index):
            if (row_index < 0 or row_index >= rows or column_index < 0 or column_index >= columns
                    or board[row_index][column_index] != "O" or visited[row_index][column_index]):
                return
            board[row_index][column_index] = "T"
            visited[row_index][column_index] = True
            convert_to_T(row_index - 1, column_index)
            convert_to_T(row_index + 1, column_index)
            convert_to_T(row_index, column_index - 1)
            convert_to_T(row_index, column_index + 1)


       # convert O to T from boarder
        for r in range(rows):
            for c in range(columns):
                if (r == 0 or r == rows - 1 or c == 0 or c == columns - 1) and board[r][c] == "O":
                    convert_to_T(r,c)

        # convert O to X
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # convert T to O
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "T":
                    board[r][c] = "O"

board =[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
solution = Solution()
solution.solve(board)

