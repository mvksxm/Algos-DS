class Solution:
    def searchMatrix(matrix: list, target: int) -> bool:
        count_row = len(matrix[0])

        l_p = 0
        r_p = count_row*len(matrix)-1

        while l_p <= r_p:
            middle_general_index = l_p + ((r_p - l_p) // 2)
            middle_row = middle_general_index // count_row
            middle_row_index = middle_general_index % count_row

            if matrix[middle_row][middle_row_index] == target:
                return True

            if matrix[middle_row][middle_row_index] < target:
                l_p = middle_general_index + 1
            elif matrix[middle_row][middle_row_index] > target:
                r_p = middle_general_index - 1

        return False

print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))