class MinStack:

    def __init__(self):
        self.stack_backend = []
        self.stack_min_value = []

    def push(self, val: int) -> None:
        self.stack_backend.append(val)

        if self.stack_min_value and val <= self.stack_min_value[-1]:
            self.stack_min_value.append(val)
        elif not self.stack_min_value:
            self.stack_min_value.append(val)

    def pop(self) -> None:

        last_elem = self.stack_backend.pop()
        if last_elem == self.stack_min_value[-1]:
            self.stack_min_value.pop()

    def top(self) -> int | None:
        if self.stack_backend:
            return self.stack_backend[-1]

        return None

    def getMin(self) -> int:
        return self.stack_min_value[-1]
