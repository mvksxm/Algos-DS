class Solution:
    def lengthOfLongestSubstring( s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 1


        l_p = 0
        r_p = l_p + 1
        window_map = {}
        window_map[s[l_p]] = 0
        global_len = 1
        local_len = 1

        while r_p < len(s):
           if s[r_p] not in window_map:
               window_map[s[r_p]] = r_p
               r_p += 1
               local_len += 1
           elif s[r_p] in window_map:
               global_len = max(global_len, local_len)
               # window_set.remove(s[r_p])
               prev_l_p = l_p
               l_p = window_map[s[r_p]] + 1
               # r_p = r_p + 1
               for i in range(prev_l_p, l_p):
                   if s[i] in window_map:
                        del window_map[s[i]]

               window_map[s[r_p]] = r_p
               window_map[s[l_p]] = l_p
               r_p = r_p + 1
               local_len = r_p - l_p

               # window_set.add(s[l_pgit


        return max(global_len, local_len)


print(Solution.lengthOfLongestSubstring("abcabcbb"))


