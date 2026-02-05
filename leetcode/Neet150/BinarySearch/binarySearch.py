
# Time Complexity: O(log(n))
# Space Complexity: O(1)

# Approach
# Implement Binary Search algorithm.


class Solution:
    def search(self, nums: list, target: int) -> int:

        l_p = 0
        r_p = len(nums) - 1

        while l_p <= r_p:

            if nums[l_p] == target:
                return l_p

            if nums[r_p] == target:
                return r_p

            middle_idx = l_p + ((r_p - l_p) // 2)
            middle_element = nums[middle_idx]

            if middle_element == target:
                return middle_idx

            if middle_element < target:
                l_p = middle_idx + 1
            else:
                r_p = middle_idx - 1

        return -1
