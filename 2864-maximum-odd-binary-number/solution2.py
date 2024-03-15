# Runtime: 34ms, Beats 81.61% of users with Python3
# Memory: 16.58MB, Beats 62.66% of users with Python3

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        return (count_one-1)*'1'+(len(s)-count_one)*'0'+'1'