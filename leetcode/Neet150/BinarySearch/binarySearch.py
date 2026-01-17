class Solution:
    def search(nums: list, target: int) -> int:
        l_p = 0
        r_p = len(nums) - 1

        while l_p <= r_p:
            middle_index = l_p + ((r_p - l_p) // 2)

            if nums[middle_index] == target:
                return middle_index

            if nums[middle_index] > target:
                r_p = middle_index - 1
            elif nums[middle_index] < target:
                l_p = middle_index + 1

        return -1

print(Solution.search([-1,0,2,4,6,8], 4))