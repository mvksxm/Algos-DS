from typing import List
from tester import Tester

# Time Complexity: O(n)*3 = O(n)
# Space Complexity: O(n) + O(n) = O(n)

# Approach
# Create two arrays: prefix_max and suffix_max. In those arrays, under a particular index store a maximum value before
# that index (in the prefix_max array) and a maximum value after that index (in the suffix_max array). Finally, iterate
# through the values in the height var and for each index calculate the amount of water that can be stored at that par-
# - ticular position make using the formula -> min(prefix_max, suffix_max) - height[i]

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        res_sum = 0

        mx = 0
        for i in range(1, len(height)):
            mx = max(mx, height[i-1])
            prefix_max[i] = mx

        mx = 0
        for i in range(len(height)-2, -1, -1):
            mx = max(height[i+1], mx)
            suffix_max[i] = mx

        for i in range(len(height)):
            elem = height[i]
            lowest_bar = min(prefix_max[i], suffix_max[i])
            diff = lowest_bar - elem
            if diff > 0:
                res_sum += diff

        return res_sum

if __name__ == "__main__":
    sl = Solution()
    tst = Tester()

    test_cases = [
        [[[0,1,0,2,1,0,1,3,2,1,2,1]], 6],
        [[[0,2,0,3,1,0,1,3,2,1]], 9]
    ]

    tst.array_test(test_cases, sl.trap)


