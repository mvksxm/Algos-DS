
def twoSum(nums: list, target: int) -> list:
    index_map = {}

    for i in range(len(nums)):
        index_map[nums[i]] = i

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in index_map and i != index_map[diff]:
            return sorted([index_map[diff], i])



print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))
print(twoSum([5,5], 10))
