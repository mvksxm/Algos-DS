# Approach - for each str in strs create a data structure in a form of an array of zeroes with the length 26
# (len 26 represents the length of an alphabet). Then iterate through each character in a particular str and increment a
# value under the index that represents the position of that particular char in an alphabet by 1 on each occurrence du -
# - ring the iteration.

# Space Complexity: O(len(strs))
# Time Complexity: O(len(strs) * len('longest str in strs'))

def groupAnagrams(strs: list):
    freq_map = {}

    for st in strs:
        freq_key_list = [0] * 26
        for char in st:
            freq_key_list[ord(char) - ord("a")] += 1

        freq_key = tuple(freq_key_list)

        if freq_key in freq_map:
            freq_map[freq_key].append(st)
        else:
            freq_map[freq_key] = [st]

    return list(freq_map.values())



# Test Cases
if __name__ == "__main__":

    tst = ["act","pots","tops","cat","stop","hat"]
    tst_result = [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
    print(sorted(groupAnagrams(tst)) == sorted(tst_result))

    tst = ["x"]
    tst_result = [["x"]]
    print(sorted(groupAnagrams(tst)) == sorted(tst_result))

    tst = [""]
    tst_result = [[""]]
    print(sorted(groupAnagrams(tst)) == sorted(tst_result))


