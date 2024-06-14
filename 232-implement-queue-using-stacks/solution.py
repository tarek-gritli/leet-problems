# Runtime: 32ms, Beats 74.87% of users with Python3
# Memory: 16.52MB, Beats 56.52% of users with Python3

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        x = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2[-1])
            self.s2.pop()
        return x

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        x = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2[-1])
            self.s2.pop()
        return x

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()