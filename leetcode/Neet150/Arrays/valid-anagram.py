def isAnagram(s: str, t: str) -> bool:
    freq = {}

    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1


    for ch in t:
        if ch in freq:
            freq[ch] -= 1
        else:
            freq[ch] = 1

        if ch in freq and freq[ch] == 0:
            del freq[ch]



    if freq:
        return False

    return True


if __name__ == "__main__":
    s1 = "jar"
    t2 = "jam"
    print(isAnagram(s1, t2))


# HashMap Solution