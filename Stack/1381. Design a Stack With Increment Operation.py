class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:

        if len(self.stack) == self.maxSize:
            return
        else:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()


    def increment(self, k: int, val: int) -> None:

        i = 0
        while i < len(self.stack) and k > 0:
            self.stack[i] += val
            i += 1
            k -= 1



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
