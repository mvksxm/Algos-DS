from tester import Tester

# Time Complexity: O(n), n = len(s)
# Space Complexity: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {"{": "}", "[":"]", "(":")"}
        par_stack = []

        for par in s:
            if par in par_map:
                par_stack.append(par_map[par])
            elif par_stack and par == par_stack[-1]:
                par_stack.pop()
            else:
                return False

        if par_stack:
            return False

        return True


if __name__ == "__main__":

    sln = Solution()
    tst = Tester()

    test_cases = [
        [["[]"],True],
        [["([{}])"],True],
        [["[(])"],False],
    ]

    tst.array_test(test_cases, sln.isValid)


