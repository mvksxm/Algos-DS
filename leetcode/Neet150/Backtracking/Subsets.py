class Solution:
    def subsets(self, nums: list) -> list:
        # [3,2,4,1]
        subsets = [[]] #[[], [1],[1, 2], [1, 2, 3],[1, 3], [2], [2,3], [3] ]

        def dfs(i, curr_sublist):
            if i >= len(nums):
                return

            modified_sublist = curr_sublist + nums[i] #[3]
            subsets.append(modified_sublist) # []
            dfs(i+1, modified_sublist)
            dfs(i+2, modified_sublist)


        for i in range(len(nums)):
            dfs(i, [])

        return subsets

    def subsetsCorrect(nums:list) -> list:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res



if __name__ == "__main__":
    nums=[3,2,4,1]
    print(Solution.subsetsCorrect(nums))

# 3 2 4 1
#                  []
#          /               \
#         []              [3]
#       /     \              \
#    []      [2]             [3,2]
#    / \     / \             /  \
#   []  [1] [2] [2,1]      [3,2][3,2,4]
#                          /     /   \
#                          [3,2,4] [3,2,4,1]

#       dfs(0, [])
#     1         2
#    /  \       |
#    2  3       3
#   /
#   3
#
#

#     3
#   /
#
#
#


