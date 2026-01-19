from typing import List
from tester import Tester

# Approach: Create a result array with the first element of the nums array already appended. It's needed, in order to
# make use of the 'prefix multip.' algorithm. Once res arr was created, iterate through the nums array by index and mul-
# tiply each element with the prev element in the res_arr list. Result of the multiplication is supposed to be inputted
# into the res_arr under the currernt iteration idx. At the end of the iteration we are supposed to put unsder the index
# n the folliowing value - res_arr[n] that equals to res_arr[n-1] * nums[n]. Such an approach makes sure that under each
# position n we have multiplication of all of the values before n and n itself.
# After first iteration, we initiate a second one that, which starts from the end of the array res_arr. On each position
# n, we multiply the prefix that is equal to the product of the elements after n with the element under the index - n-1
# that represents multiplication of all of the values before n. Such a multiplication is being performed until the ele-
# ment under the index 0, whose product except himself will be equal to the 'multiplier'.

# Space Complexity - O(1) (constant)
# Time Complexity - O(n) + O(n) = O(n) (linear)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 2:
            return [nums[1], nums[0]]

        res_arr = [nums[0]]
        for i in range(1, len(nums)):
            res_arr.append(res_arr[i-1] * nums[i])

        multiplier = 1
        for i in range(len(res_arr) - 1, -1, -1):

            if i == 0:
                res_arr[i] = multiplier
            else:
                res_arr[i] = multiplier * res_arr[i-1]
                multiplier *= nums[i]


        return res_arr


if __name__ == "__main__":
    sln = Solution()
    tester = Tester()

    tests = [
        [[-1,0,1,2,3], [0, -6, 0, 0, 0]],
        [[1,2,4,6], [48, 24, 12, 8]]
    ]

    tester.array_test(tests, sln.productExceptSelf)