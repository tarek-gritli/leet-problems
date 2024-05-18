# Runtime: 24ms, Beats 98.05% of users with Python3
# Memory: 16.53MB, Beats 72.65% of users with Python3

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        x = self.q[-1]
        self.q.pop()
        return x

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()