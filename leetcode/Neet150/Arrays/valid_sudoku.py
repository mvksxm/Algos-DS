from typing import List
from tester import Tester


# n -> rows; n -> cols
# Time Complexity: O(n*n) + O(n*n) = O(n*n)
# Space Complexity: O(n*n) + O(n*n) = O(n*n)

# Approach: First iteration - going over the rows. For each row add a row item to the row_col_set and, in case if
# row elem is in the set -> return False. When accessing a new row during the iteration -> clear the row_col_set.
# In parallel the matrix_set is being maintained as well, that contains 3 sets - 1 per specific 3x3 matrix. Elements
# to the matrix_set are being added according to their col index. Specifically - 0 elem idx = 0 // 3 = 0 (index of the
# set in the matrix_set, where elem will be appended) and, for example, 8 // 3 = 2 (another index of the set where elem
# will be appended). On the row under the index 3 - matrix_sets var will be reset, due to the fact that new 3x3 matrices
# appear on the board. In case, if an elem already exists in the set under respective idx in the matrix_sets var, then
# return False, because it means that elem appeared twice in a particular 3x3 matrix.
# Second iteration -> going over the columns. On each column iteration a set row_col_set is being populated with the unique elems in
# a column. In case, if elem already exists in the set -> return False. set is being reset on every iteration.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_col_set = set()
        matrix_sets = [set() for _ in range(3)]

        # Row Column Iteration
        for r in range(len(board)):

            if r % 3 == 0:
                matrix_sets = [set() for _ in range(3)]

            for c in range(len(board[r])):
                matrix_set_idx = c // 3
                digit = board[r][c]

                if digit != "." and (digit in matrix_sets[matrix_set_idx] or digit in row_col_set):
                    return False

                if digit != ".":
                    matrix_sets[matrix_set_idx].add(digit)
                    row_col_set.add(digit)

            row_col_set.clear()

        # Columns Iteration
        for c in range(len(board[0])):
            for r in range(len(board)):

                col_elem = board[r][c]

                if col_elem != "." and col_elem in row_col_set:
                    return False

                if col_elem != ".":
                    row_col_set.add(col_elem)

            row_col_set.clear()

        return True

if __name__ == "__main__":
    sl = Solution()
    tst = Tester()

    test_cases = [
        [
            [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]],
            True
         ],
        [
            [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","1",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]],
            False
        ]
    ]

    tst.array_test(test_cases, sl.isValidSudoku)
