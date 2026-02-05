
# Time Complexity: O(log(m*n)); m -> rows, n -> cols
# Space Complexity: O(1)

# Approach
# Implement Binary Search on top of the m*n matrix. Create left pointer 0 and right pointer -> (len(m) * len(n)) - 1.
# For each pointer calculate its respective row and column by using the following formulas: 1) For row -> pointer // len(n);
# 2) For col -> pointer % len(n). It's needed in order to access the value under the pointer itself for further comparison.

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:

        l_p = 0
        r_p = len(matrix) * len(matrix[0]) - 1

        def calculate_row(p): return p // len(matrix[0])
        def calculate_col(p): return p % len(matrix[0])


        while l_p <= r_p:

            l_row = calculate_row(l_p)
            l_column = calculate_col(l_p)

            r_row = calculate_row(r_p)
            r_column = calculate_col(r_p)

            middle_idx = l_p + ((r_p - l_p) // 2)
            middle_row = calculate_row(middle_idx)
            middle_col = calculate_col(middle_idx)

            if matrix[l_row][l_column] == target:
                return True

            if matrix[r_row][r_column] == target:
                return True

            if matrix[middle_row][middle_col] == target:
                return True

            if matrix[middle_row][middle_col] < target:
                l_p = middle_idx + 1
            else:
                r_p = middle_idx - 1

        return False










# print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
# print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))