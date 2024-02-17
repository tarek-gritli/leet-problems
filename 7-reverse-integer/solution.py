# Runtime: 34ms, Beats 76.41% of users with Python3
# Memory: 16.61MB, Beats 56.18% of users with Python3

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
            if x >= pow(2,31):
                return 0
            return x
        x=int(str(-x)[::-1]) * -1
        if x < pow(2,31) * -1:
            return 0
        return x