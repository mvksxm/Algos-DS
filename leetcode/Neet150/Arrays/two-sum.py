# Approach: use a map to store single values as keys and their respective indexes as values.
# On each iteration through the nums array, check if the diff between target and current num in the map already. In case,
# if it is - return an index of the remainder first and then of the current value itself

# Space complexity: O(n)
# Time complexity: O(n)


def twoSum(nums: list, target: int) -> list:
    num_index_map = {}

    for i in range(len(nums)):

        to_add = target - nums[i]
        if to_add in num_index_map:
            return [num_index_map[to_add], i]

        num_index_map[nums[i]] = i

    return []




print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))
print(twoSum([5,5], 10))
