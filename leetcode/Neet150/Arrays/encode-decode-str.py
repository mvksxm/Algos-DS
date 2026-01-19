from typing import List

# Approach: encoding of each string should be at its beginning. Specifically, first element of an encoded string should
# be len of an integer the represents string's len, then a len integer should be inputted and, in the end, a string
# itself. That encoding process should be repeated for each string. Decoding should be performed step by step. First,
# we check the len of string's len, by using that info we extract a needed number of characters and identify it as a
# len of a string. And, in the end, by using that length, we are inputting a string to a decoded list.

# m -> max length of an element in the strs array.
# n -> length  of strs
# Space Complexity: O(n) + O(n) = O(n) (linear)
# Time Complexity: O((m+m)*n) + O(m*n + (n*4)) = O(m*n) (linear)

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            str_len = str(len(string))
            len_of_len = str(len(str_len))
            encoded_str += (len_of_len + str_len + string)

        return encoded_str

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        decoded_list = []
        count_len_idx = 0
        while count_len_idx < len(s):
            str_start_idx = count_len_idx + 1 + int(s[count_len_idx])
            str_len = s[count_len_idx + 1 : str_start_idx]
            str_finish_idx = str_start_idx + int(str_len)
            decoded_str = s[str_start_idx:str_finish_idx]
            decoded_list.append(decoded_str)
            count_len_idx = str_finish_idx

        return decoded_list


if __name__ == "__main__":
    sol = Solution()
    enc_str = sol.encode(["we","say",":","yes","!@#$%^&*()"])
    print(enc_str)
    print(sol.decode(enc_str))
