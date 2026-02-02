from tester import Tester

# Time Complexity: O(n)
# Space Complexity: O(m), where m is the amount of unique characters in a string s

# Approach:
# Create a window and a hashmap that will store unique characters present in a string in the form of char -> idx. Then,
# r_border of a window should expand, in case, if r_border element is not present in a hashmap or r_border element already
# present, but its index is smaller than the l_border (means element is not present in the current window) - continue win
# dow iteration. In case, if element is in a hashmap and its index bigger than l_border (element in a window), it means
# that we've found a duplicate. In that case, max should be updated with the window's max length until the duplicate
# was encountered, l_border of the window should be shifted to the duplicate_idx + 1 (so that we wouldn't have no more
# duplicates). Finally duplicate's idx in a hashmap should be updated to the latest encountered idx, so that we were
# able to catch a repetition for this value in a current window as well.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        char_map = {s[0]: 0}
        max_len = 1

        l_border = 0
        r_border = 1

        while r_border < len(s):

            r_element = s[r_border]

            if r_element not in char_map:
                char_map[r_element] = r_border
            elif r_element in char_map and char_map[r_element] < l_border:
                char_map[r_element] = r_border
            else:
                max_len = max(max_len, r_border - l_border)
                duplicate_idx = char_map[r_element]
                l_border = duplicate_idx + 1
                char_map[r_element] = r_border

            r_border += 1

        max_len = max(max_len, r_border - l_border)
        return max_len


if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [["zxyzxyz"], 3],
        [["xxxx"], 1],
        [["dvdf"], 3]
    ]

    tst.array_test(test_cases, sln.lengthOfLongestSubstring)


