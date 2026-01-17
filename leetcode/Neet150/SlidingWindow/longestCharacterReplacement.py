class Solution:
    def characterReplacementBruteForce(s: str, k: int) -> int:

        max_len = 0
        for i in range(len(s)):
            local_len = 1
            n = k
            for j in range(i+1, len(s)):
                if s[j] == s[i] and n >= 0:
                    local_len += 1
                elif s[j] != s[i] and n > 0:
                    local_len += 1
                    n -= 1
                else:
                    # max_len = max(local_len, max_len)
                    break

            if i > 0 and n>=0:
                for j in range(i-1, -1, -1):
                    if s[j] == s[i] and n >= 0:
                        local_len += 1
                    elif s[j] != s[i] and n > 0:
                        local_len += 1
                        n -= 1
                    else:
                        # max_len = max(local_len, max_len)
                        break

            max_len = max(local_len, max_len)


        return max_len


    # def characterReplacementSlidingWindow(s: str, k: int) -> int:
    #     if not s:
    #         return 0
    #
    #     if len(s) == 1:
    #         return 1
    #
    #     freq_dict = {s[0]:1}
    #     most_freq_element = None
    #     global_cnt = 0
    #     local_cnt = 0
    #     l_p = 0
    #     r_p = l_p + 1
    #     n = k
    #
    #     while r_p < len(s):
    #
    #         if s[l_p] == s[r_p] and n>=0:
    #             local_cnt += 1
    #             freq_dict[s[l_p]] += 1
    #
    #             if not most_freq_element or freq_dict[s[l_p]]>=freq_dict[most_freq_element]:
    #                 most_freq_element = s[l_p]
    #
    #         elif s[l_p] != s[r_p] and n>0:
    #             local_cnt += 1
    #             n -= 1
    #             if s[r_p] not in freq_dict:
    #                 freq_dict[s[r_p]] = 1
    #             else:
    #                 freq_dict[s[r_p]] += 1
    #
    #             if not most_freq_element or freq_dict[s[r_p]]>=freq_dict[most_freq_element]:
    #                 most_freq_element = s[r_p]
    #         else:
    #             global_cnt = max(local_cnt, global_cnt)
    #
    #             if s[l_p]
    #
    #
    #         max_len = max(local_len, max_len)


print(Solution.characterReplacementBruteForce("AACBABBA", 2))
print(Solution.characterReplacementBruteForce("XYYX", 2))
print(Solution.characterReplacementBruteForce("AAABABB", 1))
print(Solution.characterReplacementBruteForce("ABAB", 2))
print(Solution.characterReplacementBruteForce("ABBB", 2))







