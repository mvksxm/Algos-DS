from typing import List
from tester import Tester

# Time Complexity
# n = len(numbers); O(n)

# Space Complexity
# O(1)

# Approach
# Create two pointers, one starting at index 0, another at the index len(numbers) - 1. On each iteration sum digits from
# both pointers. In case, if sum > target - move right pointer to the left, if sum < target - move left pointer to the
# right. In case if sm == target - return.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l_p = 0
        r_p = len(numbers) - 1

        while l_p < len(numbers) and r_p >= 0:
            l_element = numbers[l_p]
            r_element = numbers[r_p]

            sm = l_element + r_element

            if sm == target:
                return [l_p + 1, r_p + 1]
            elif sm > target:
                r_p -= 1
            else:
                l_p += 1

        return []

if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    tests = [
        [[[1,2,3,4], 3], [1, 2]]
    ]

    tst.array_test(tests, sln.twoSum)