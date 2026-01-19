# HashMap Solution
# Space complexity O(n) - linear time
# Time Complexity O(s + t) - linear time

def isAnagram(s: str, t: str) -> bool:
    freq_map = {}

    for char in s:
        if char not in freq_map:
            freq_map[char] = 1
        else:
            freq_map[char] += 1

    for char in t:
        if char in freq_map:
            freq_map[char] -= 1

            if freq_map[char] == 0:
                del freq_map[char]
        else:
            return False

    if not freq_map:
        return True

    return False



if __name__ == "__main__":
    s1 = "jar"
    t2 = "raj"
    print(isAnagram(s1, t2))