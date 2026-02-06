from typing import List

from tester import Tester


# Time Complexity: O(log(n))
# Space Complexity: O(1)

# Approach
# Use Binary Search for the nums array. In case if mid_element is the smaller between the pointers - right_pointer = middle_pointer - 1\
# It's needed, because we assume that all smaller elements will be to the left side from the smallest value encountered
# during the current iteration. In case, if left_pointer is the smallest (we can safely assume that the first element is the min).
# Otherwise, in case, if right pointer is the smallest set the left_pointer = middle_pointer + 1

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l_p = 0
        r_p = len(nums) - 1
        min_res = 1001

        while l_p <= r_p:

            m_p = l_p + ((r_p - l_p) // 2)
            mid_val = nums[m_p]
            min_res = min(min_res, mid_val)

            if mid_val <= nums[r_p] and mid_val <= nums[l_p]:
                r_p = m_p - 1
            elif nums[r_p] < mid_val and nums[r_p] < nums[l_p]:
                l_p = m_p + 1
            elif nums[l_p] < mid_val and nums[l_p] < nums[r_p]:
                r_p = m_p - 1


        return min_res


if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [[[6, 1, 2, 3, 4, 5]], 1],
        [[[4, 5, 6, 1, 2, 3]], 1],
        [[[1,2,3,4,5,6]], 1],
        [[[3,4,5,6,1,2]], 1],
    ]

    tst.array_test(test_cases, sln.findMin)
