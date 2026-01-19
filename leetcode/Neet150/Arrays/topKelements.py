from typing import List

# Approach: count the frequency of numbers in array by using a hashmap, iterate thorough that map and create a new one
# with frequencies as keys and numbers as values. During creation of a new one get a max freq, and then iterate from it
# backwards until 0 and check if the res array already has length of k. Once length equal to k -> return the res


# n -> number of elems in nums
# m -> number of unique elems in nums
# Space Complexity: O(m) + O(m) + O(1) + O(k) = linear time
# Time Complexity: O(n) + O(m) + O(k) = linear time

def topKFrequent(nums: List[int], k: int) -> List[int]:

    if not nums:
        return []

    num_freq_map = {}
    freq_num_map = {}


    for n in nums:
        if n in num_freq_map:
            num_freq_map[n] += 1
        else:
            num_freq_map[n] = 1

    max_freq = 1
    for num, freq in num_freq_map.items():
        if freq in freq_num_map:
            freq_num_map[freq].append(num)
        else:
            freq_num_map[freq] = [num]

        max_freq = max(max_freq, freq)

    res = []
    for i in range(max_freq, 0, -1):
        if i in freq_num_map:
            for num in freq_num_map[i]:
                if len(res) == k:
                    return res
                res.append(num)

    return res









if __name__ == "__main__":

    tst = [1,2,2,3,3,3]
    tst_k = 2
    res = [2,3]

    print(sorted(topKFrequent(tst,  tst_k)) == res)

    tst = [7,7]
    tst_k = 1
    res = [7]
    print(sorted(topKFrequent(tst,  tst_k)) == res)

