class Solution:
    def isValid( s: str) -> bool:

        stack = []
        parentheses_map = {"(":")",  "{":"}", "[":"]"}


        for par in s:
            if stack and stack[-1] == par:
                stack.pop()
            elif par in parentheses_map:
                stack.append(parentheses_map[par])
            else:
                return False

        return False if stack else True

print(Solution.isValid("[]"))
print(Solution.isValid("([{}])"))
print(Solution.isValid("[(])"))
print(Solution.isValid("[(])"))
print(Solution.isValid("]"))