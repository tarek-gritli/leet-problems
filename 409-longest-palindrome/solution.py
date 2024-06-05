# Runtime: 36ms, Beats 61.99% of users with Python3
# Memory: 16.65MB, Beats 34.10% of users with Python3
            
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i],0)+1
        doubles = 0
        singles = 0
        for letter,value in m.items():
            if value % 2 == 0:
                doubles+=value
            else:
                doubles+=value-1
                singles = 1
        if singles:
            return doubles + 1
        return doubles