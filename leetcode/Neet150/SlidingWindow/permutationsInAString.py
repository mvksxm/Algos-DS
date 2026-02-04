from tester import Tester

# Time Complexity: O(n)
# Space Complexity: O(m); m = len(s1)

# Approach
# Frequency map of the characters in s1 is created and a copy of it as well for the modifications during the main window iteration.
# During the main window iteration, characters, which are located in the freq_map are being removed from the freq_map_op_copy,
# so that, in case, if freq_map_op_copy would end up empty - it would mean that a permutation was located. Window is moved only
# then, when ( i+1 // len(s1) >= 1 ) or just ( i+1 >= len(s1) ). If condition is true, we assume that the max len of the window,
# that is supposed to be investigated, was reached and the window can move one idx further.

# Window Iteration
# The main complexity here is freq_map_op_copy manipulation. When window moves further, element under the right idx is
# being either removed from the map (in case if its frequency is 0) or 1 is subtracted from its frequency. At the same time,
# element under the left idx is being added to the map or its frequency is increased, signalizing that element of the
# permutation left the window and that it would need to be decremented further along the iteration of the window. Also,
# it's important to note that, in case if there are two elements of 'a' in the analyzed substring (example - ada), but
# we are supposed to locate the permutation of 'abc'. freq_map_op_copy would look like this - {"a":-1, b:1, c:1}. It means, that
# in order to fulfill the requirement of having one 'a' in the permutation we need remove one 'a' from the analyzed per-
# -mutation and respectively add it to the freq_map_op_copy. In that case, during the next window iteration, map would
# end up looking like this {"a":0, "b":1, "c":1} = {"b":1, "c":1}. It means that the 'a' requirement was fulfilled and
# right now we need to find "b", "c" and pop them from the map as well.

class Solution:
    def checkInclusionPersonal(self, s1: str, s2: str) -> bool:

        if len(s2) == 1 and s1 == s2: return True

        # Populate freq map
        freq_map = {}
        for char in s1:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1

        freq_map_op_copy = freq_map.copy()
        perm_len = len(s1)

        for i in range(len(s2)):

            r_element = s2[i]

            if r_element in freq_map_op_copy:
                future_value = freq_map_op_copy[r_element] - 1
                if future_value == 0:
                    del freq_map_op_copy[r_element]
                else:
                    freq_map_op_copy[r_element] -= 1
            elif r_element in freq_map:
                freq_map_op_copy[r_element] = -1

            if not freq_map_op_copy:
                return True

            if (i+1) // perm_len > 0:

                l_element = s2[(i+1) - perm_len]

                if (
                    l_element in freq_map
                    and l_element in freq_map_op_copy
                ):
                    if freq_map_op_copy[l_element] == -1:
                        del freq_map_op_copy[l_element]
                    else:
                        freq_map_op_copy[l_element] += 1
                elif l_element in freq_map:
                    freq_map_op_copy[l_element] = 1

        return False


if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [["abc", "lecabee"], True],
        [["abc", "lecaabee"], False],
        [["ab", "eidbaooo"], True],
        [["ab", "eidboaoo"], False]
    ]

    tst.array_test(test_cases, sln.checkInclusionPersonal)

