from typing import List

# Time Complexity: O(log(n))
# Space Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        array_len = len(nums)
        l_p = 0
        r_p = array_len - 1

        # Searching for a pivot
        while l_p < r_p:
            m = (l_p + r_p) // 2
            if nums[m] > nums[r_p]:
                l_p = m + 1
            else:
                r_p = m

        pivot_idx = l_p
        l: int
        r: int
        if nums[pivot_idx] <= target <= nums[array_len - 1]:
            l = pivot_idx
            r = array_len - 1
        else:
            l = 0
            r = pivot_idx - 1

        # Searching for an element
        while l <= r:
            mid = l + ((r - l) // 2)
            mid_elem = nums[mid]

            if mid_elem == target:
                return mid
            elif mid_elem > target:
                r = mid - 1
            else:
                l = mid + 1


        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.search([3,4,5,6,1,2], 1))
    print(sln.search([3,5,6,0,1,2], 4))