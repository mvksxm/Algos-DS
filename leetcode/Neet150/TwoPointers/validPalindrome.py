
# Time Complexity:
# n = len(s)
# O(n) + O(n) = O(n)

# Space Complexity:
# O(1)

# Approach
# Create two pointers, one from the right side, another one from the left side of the string. Move pointers on each ite-
# -ration of the while loop (right one to the left, left one to the right). In case, if character in a string is not al-
# -phanumeric move pointer further until an alphanumeric character would appear in a string.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_p = 0
        r_p = len(s) - 1

        while l_p < len(s) and r_p >= 0:
            l_element = s[l_p].lower()
            r_element = s[r_p].lower()

            if not l_element.isalnum():
                l_p += 1
                continue

            if not r_element.isalnum():
                r_p -= 1
                continue

            if l_element != r_element:
                return False

            l_p += 1
            r_p -= 1


        return True

if __name__ == "__main__":
    sol = Solution()
    tst1 = "Was it a car or a cat I saw?"
    tst2 = "tab a cat"
    print(sol.isPalindrome(tst1))
    print(sol.isPalindrome(tst2))




