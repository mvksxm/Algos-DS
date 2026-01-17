from typing import List


def topKFrequent( nums: List[int], k: int) -> List[int]:
    count_map = {}
    count_arr = [[]] * (len(nums) + 1)

    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1


    for key, val in count_map.items():

        if count_arr[val]:
            count_arr[val].append(key)
        else:
            count_arr[val] = [key]

    output_arr = []
    i = len(nums)
    while i>=0 and k>0:
        if count_arr[i]:
            for num in count_arr[i]:
                output_arr.append(num)
                k -= 1

        i -= 1

    return output_arr


print(topKFrequent([7,7], 1))
