class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.minstack):
            self.minstack.append(
                min(self.minstack[-1], val)
            )
        else:
            self.minstack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        self.minstack = self.minstack[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
