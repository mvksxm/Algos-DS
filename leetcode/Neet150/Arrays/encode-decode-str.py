class Solution:

    def encode(strs: list) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += (str(len(st)) + "#" + st)

        return encoded_str

    def decode(s: str) -> list :
        decoded_arr = []

        i = 0
        j = 0
        while i<len(s):
            if s[i] == "#":
                num_steps = int(s[j:i])
                decoded_arr.append(s[i+1:i+1+num_steps])
                j = i+1+num_steps
                i = j + 1
            else:
                i+=1

        return decoded_arr


encoded_str = Solution.encode(["we","say",":","yes"])
print(Solution.decode(encoded_str))
