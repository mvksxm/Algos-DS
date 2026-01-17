def groupAnagrams( strs: list):
    pattern_freq = {}

    for st in strs:

        pattern = [0]*26

        for ch in st:
            ch_index = ord(ch) - ord('a')
            pattern[ch_index] += 1

        pattern = str(pattern)

        if pattern in pattern_freq:
            pattern_freq[pattern].append(st)
        else:
            pattern_freq[pattern] = [st]

    result_arr = []

    for key,value in pattern_freq.items():
        result_arr.append(value)

    return result_arr

print(groupAnagrams(["ddddddddddg","dgggggggggg"]))


