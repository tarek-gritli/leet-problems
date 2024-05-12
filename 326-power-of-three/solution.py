# Runtime: 47ms, Beats 97.74% of users with Python3
# Memory: 16.65MB, Beats 22.54% of users with Python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        else:
            return n%3==0 and self.isPowerOfThree(n//3)