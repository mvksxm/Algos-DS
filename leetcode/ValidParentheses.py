
# Stack implementation and hashMap approach
class Solution:
    def isValid(self, s: str) -> bool:
        # ([{}])
        hashMap = {"}":"{", "]":"[", ")":"("}
        if s[0] not in hashMap:
            stack = [s[0]]
        else:
            return False

        for i in range(1, len(s)):
            if hashMap.get(s[i]) and stack and stack[-1] == hashMap.get(s[i]):
                stack.pop()
            else:
                stack.append(s[i])

        if stack:
            return False

        return True