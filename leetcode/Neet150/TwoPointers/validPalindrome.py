
class Solution:
    def isPalindrome(s: str) -> bool:
        fp = 0
        preprocessed_string = s.lower().replace(" ", "")
        bp = len(preprocessed_string) - 1

        while (fp < bp):

            if not preprocessed_string[fp].isalnum():
                fp += 1
                continue

            if not preprocessed_string[bp].isalnum():
                bp -= 1
                continue

            if preprocessed_string[fp] != preprocessed_string[bp]:
                return False

            fp += 1
            bp -= 1

        return True


s = "0P"
print(Solution.isPalindrome(s))