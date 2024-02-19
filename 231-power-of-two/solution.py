# Runtime: 35ms, Beats 69.97% of users with Python3
# Memory: 16.47MB, Beats 96.02% of users with Python3

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n & (n-1) == 0