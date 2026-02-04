
# Time Complexity: O(1)
# Space Complexity: O(n)

# Approach
# Maintain two stacks. One for all the values, another one for min values only. Min Stack should be populated only
# if current value is less than or equal to the one, which is currently on top of the stack. Usual stack should be po -
# - pulated as it is.
# In case, if value that is being popped from the main stack is also on top of the min stack, pop the min value as well.

class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = [2**31]

    def push(self, val: int) -> None:

        if val <= self._min_stack[-1]:
            self._min_stack.append(val)

        self._stack.append(val)

    def pop(self) -> None:

        if not self._stack:
            return None

        if self._stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()

        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1] if self._stack else None

    def getMin(self) -> int:
        return self._min_stack[-1]