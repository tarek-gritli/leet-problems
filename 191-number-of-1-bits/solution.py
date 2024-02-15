# Runtime: 37ms, Beats 53.54% of users with Python3
# Memory: 16.47MB, Beats 90.89% of users with Python3

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)
        bits=[bit for bit in binary if bit == '1']
        return len(bits)