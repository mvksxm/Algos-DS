class Solution:
    def combinationSum2(candidates: list, target: int) -> list:
        res = []
        candidates.sort()

        subset = []
        def dfs(idx, curr_sum):

            if curr_sum == target:
                res.append(subset.copy())
                return

            if idx >= len(candidates) or curr_sum > target:
                return

            subset.append(candidates[idx])
            dfs(idx+1, curr_sum + candidates[idx])
            subset.pop()

            while idx <= len(candidates) - 2 and candidates[idx] == candidates[idx+1]:
                idx += 1

            dfs(idx+1, curr_sum)

        dfs(0, 0)

        return res


if __name__ == "__main__":
    print(Solution.combinationSum2([9,2,2,4,6,1,5], 8))


#   [1,2,2,4,5,6,9]   t = 8

#          1
#        /
#       3
#      / \
#     5   7
#    / \
#   9   10

#        []
#       /          \
#      [1]           [ ]
#      /  \
#   [1,2,2]  [1]
#    /
#  [1,2,2,4]
#
#
#


