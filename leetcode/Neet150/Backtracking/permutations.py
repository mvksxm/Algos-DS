

class Solution:
    def permute(nums: list) -> list:
        res = []

        subset = []
        visited = set()

        def dfs(idx:int, visited_set:set):
            visited_set.add(idx)
            subset.append(nums[idx])

            if len(nums) == len(visited):
                res.append(subset.copy())
                return

            allowed_visit = [j for j in range(len(nums)) if j!=idx and j not in visited_set]
            for j in allowed_visit:
                dfs(j, visited_set)
                subset.pop()
                visited_set.remove(j)


        for i in range(len(nums)):
            dfs(i, visited)
            subset = []
            visited = set()

        return res

if __name__ == "__main__":
    nums = [7]
    print(Solution.permute(nums))
# visited = set()
# [1,2,3]
# [1,2,3,4,5]i+1
# res= [[1,2,3,4,5], [1,2,3,5,4],[1,2,4,3,5], [1,2,4,3,5], [1,2,4,5,3]
# 1st call: i+=1
# 2nd call: i+=2
# curr=3
# visited = [1,2,3]
