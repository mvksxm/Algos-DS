from tester import Tester

# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: define the rules to make the substring valid, specifically, we need to make sure on each window that
# (len(window) - max_freq_elem <= k) formula is valid.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s: return 0
        if len(s) == 1: return 1

        res = 0

        l_border = 0
        r_border = 1
        r_changed = True

        max_freq = 1
        max_freq_element = s[l_border]

        freq_map = {s[l_border]: 1}

        while r_border < len(s):

            r_element = s[r_border]
            window_width = (r_border - l_border) + 1

            if r_changed and r_element in freq_map:
                freq_map[r_element] += 1
            elif r_changed and r_element not in freq_map:
                freq_map[r_element] = 1

            if freq_map[r_element] >= max_freq:
                max_freq = freq_map[r_element]
                max_freq_element = r_element

            if window_width - max_freq <= k:
                res = max(res, window_width)
                r_border += 1
                r_changed = True
            else:
                exclude_elem = s[l_border]

                if exclude_elem == max_freq_element:
                    max_freq -= 1

                freq_map[exclude_elem] -= 1
                l_border += 1
                r_changed = False

        return res

if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [["BAAA", 0], 3],
        [["XYYX", 2], 4],
        [["AAABABB", 1], 5]
    ]

    tst.array_test(test_cases, sln.characterReplacement)







