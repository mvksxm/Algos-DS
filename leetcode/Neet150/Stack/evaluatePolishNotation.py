class Solution:
    def evalRPN(tokens:  list) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        # expr_value = None

        for tkn in tokens:
            if tkn in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(Solution.operationExecution(tkn, val1, val2))

            else:
                stack.append(tkn)

        return stack[-1]

    def operationExecution(operator, val1, val2):
        val1 = int(val1)
        val2 = int(val2)

        if operator == "+":
            return val1 + val2

        if operator == "-":
            return val1 - val2

        if operator == "*":
            return val1 * val2

        if operator == "/":
            return int(val1 / val2)

        return None


print(Solution.evalRPN(["2","1","+","3","*"]))
print(Solution.evalRPN(["4","13","5","/","+"]))
print(Solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(Solution.evalRPN(["3","11","+","5","-"]))