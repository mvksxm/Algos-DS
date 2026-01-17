class Solution:
    def longestConsecutive(nums: list) -> int:
        pass
        # 2:1, 20:1, 4:3, 10:1, 3:2, 5:4

        # 0:1, 3:2, 2:1, 5:4, 4:3, 6:5, 1:2
        # 0:1, 3:2, 2:3, 5:4, 8:2, 4:3,6:5, 7:6, 1:2

        count_map = {}

        # for num in nums:
        #
        #     if num in count_map:
        #         continue
        #
        #     if num not in count_map and num-1 in count_map:
        #         count_map[num] = count_map[num-1] + 1
        #     elif num not in count_map:
        #         count_map[num] = 1
        #
        #     if num+1 in count_map:
        #         count_map[num+1] += count_map[num]
        #
        # for key in count_map:
        #     if key - 1 in count_map:
        #         count_map[key] = count_map[key-1] + 1
        #     if key + 1 in count_map:
        #         count_map[key+1] = count_map[key] + 1

        nums_set = set(nums)
        heads = []
        for num in nums_set:
            if num - 1 not  in nums_set:
                heads.append(num)

        mx_len = 0
        for head in heads:
            curr_num = head
            seq_len = 1
            while curr_num + 1 in nums_set:
                curr_num = curr_num + 1
                seq_len += 1

            mx_len = max(seq_len, mx_len)



        print(mx_len)
        return mx_len



Solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
