
# O(n) solution two pointers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        p1 = 0
        p2 = len(str(x)) - 1

        # 2 1 1 2
        while p1 < p2:
            if str_num[p1] != str_num[p2]:
                return False

            p1+=1
            p2-=1

        return True