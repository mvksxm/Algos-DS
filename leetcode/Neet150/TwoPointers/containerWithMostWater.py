from typing import List
from tester import Tester

# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach (Two Pointers)
# Define left pointer, right pointer and the var that will hold the sum of the water between two bars. On each iteration
# calculate the sum of the water between bars and update the global sum, in case, if local one is bigger. After updating
# the sum, iterate the pointer that holds the value smaller than the one held by another pointer. In case, if two values
# are equal - iterate both of the pointers.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l_p = 0
        r_p = len(heights)-1

        while l_p < r_p:
            min_bar = min(heights[l_p], heights[r_p])
            max_water = max(max_water, min_bar * (r_p - l_p))

            if heights[l_p] > heights[r_p]:
                r_p -= 1
            elif heights[r_p] > heights[l_p]:
                l_p += 1
            else:
                r_p -= 1
                l_p += 1

        return max_water


if __name__ == "__main__":

    sl = Solution()
    tst = Tester()

    test_cases = [
        [[[1,7,2,5,4,7,3,6]], 36],
        [[[2,2,2]], 4]
    ]

    tst.array_test(test_cases, sl.maxArea)





