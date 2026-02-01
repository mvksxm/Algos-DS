from typing import List
from tester import Tester

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


