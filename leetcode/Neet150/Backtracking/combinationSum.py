class Solution:
    def combinationSumMySolution(nums: list, target: int) -> list:

        res = []
        subset = []

        def dfs(num_index, target_val):

            nums_elem = nums[num_index]
            subset.append(nums_elem)
            target_val -= nums_elem

            if target_val == 0:
                res.append(subset.copy())
                return

            if target_val < 0:
                return

            elements_consider = [j for j in range(num_index, len(nums)) if target_val >= nums[j]]
            # if not elements_consider:
            #     subset.pop()
            #

            for elem_ind in elements_consider:
                dfs(elem_ind, target_val)
                subset.pop()


        for i in range(len(nums)):
            subset = []
            dfs(i, target)

        return res

if __name__ == "__main__":
    nums = [3,4,5]
    t = 16
    print(Solution.combinationSumMySolution(nums, t))


    # [2, 5, 6, 9 ]; t = 9
        # result = [2, 2, 5]
        #
# 2 2
#[2,4,5,8] t = 8
#            2
#          /   \       \  \
#         2      4      5  8
#        / |     / \
#       2  4     2  4
#      /        /
#     2         2
#