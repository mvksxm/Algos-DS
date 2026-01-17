class Solution:
    def productExceptSelf(nums: list) -> list:

        if not nums:
            return []

        if len(nums) == 1:
            return nums


        prefix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)

        output_array = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            # suffix_array[i] = product_array[i] * nums[i+1] * (product_array[i + 1] if i + 1 < len(nums)-1 else 1)
            suffix_array[i] = suffix_array[i+1] * nums[i+1]

        for i in range(len(nums)):
            output_array[i] = prefix_array[i] * suffix_array[i]



        return output_array


print(Solution.productExceptSelf([-1,0,1,2,3]))