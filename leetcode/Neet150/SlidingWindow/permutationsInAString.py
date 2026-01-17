class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        freq_dict = {}

        for ch in s1:
            if ch not in freq_dict:
                freq_dict[ch] = 1
            else:
                freq_dict[ch] += 1

        local_copy = freq_dict.copy()

        l_p = 0
        r_p = l_p + len(s1) - 1
        #
        while r_p < len(s2):
            for i in range(l_p, r_p + 1):

                if s2[i] in local_copy and local_copy[s2[i]] == 1:
                    del local_copy[s2[i]]
                elif s2[i] in local_copy and local_copy[s2[i]] > 1:
                    local_copy[s2[i]] -= 1
                elif s2[i] not in local_copy:
                    break

            if not local_copy:
                return True

            local_copy = freq_dict.copy()
            l_p += 1
            r_p += 1

        return False


print(Solution.checkInclusion("abc", "lecabee"))
print(Solution.checkInclusion("abc", "lecaabee"))
print(Solution.checkInclusion("ab", "eidbaooo"))
print(Solution.checkInclusion("ab", "eidboaoo"))

