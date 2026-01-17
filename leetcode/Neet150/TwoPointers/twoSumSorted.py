class Solution:
    def twoSum(numbers: list, target: int) -> list:
        i = 0
        j = 1

        while j<len(numbers) and i<j:

            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]


            if numbers[i] + numbers[j] < target:
                i+=1
                j+=1
            elif numbers[i] + numbers[j] > target:
                 i-=1

        return []

    # [1, 3, 8, 12, 13, 14, 20, 21]
    # 22


print(Solution.twoSum([1, 2, 3, 4], 3))