import math
from tester import Tester

# Time Complexity: O(n)
# Space Complexity: O(m); m - amount of numbers in tokens

# Approach
# Iterate through the tokens and add numbers to the stack until the mathematical operator would be encountered. Once
# it is encountered - pop two top items from the stack, perform mathematical operation and add the result back on top
# of the stack. Perform the same logic until the end of the tokens list.

class Solution:
    def evalRPN(self, tokens: list) -> int:

        if len(tokens) == 1: return int(tokens[0])

        stack = []
        operators_set = {"+", "-", "*", "/"}

        for tkn in tokens:
            if tkn not in operators_set:
                stack.append(int(tkn))
            else:
                second_element = stack.pop()
                first_element = stack.pop()
                processed_element = self._perform_operation(tkn,first_element, second_element)
                stack.append(processed_element)

        return stack[-1]


    def _perform_operation(self, operand, *digits) -> int:

        if operand == "+":
            return digits[0] + digits[1]

        if operand == "-":
            return digits[0] - digits[1]

        if operand == "*":
            return digits[0] * digits[1]

        if operand == "/":
            return math.trunc(digits[0] / digits[1])

        raise Exception(f"Invalid operand - {operand}!")


if __name__ == "__main__":
    sln = Solution()

    tst = Tester()
    test_cases = [
        [[["10","6","9","3","+","-11","*","/","*","17","+","5","+"]], 22],
        [[["1","2","+","3","*","4","-"]], 5]
    ]
    tst.array_test(test_cases,sln.evalRPN)


