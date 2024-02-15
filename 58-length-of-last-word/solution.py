# Runtime: 38ms, Beats 42.53% of users with Python3
# Memory: 16.61MB Beats 61.98% of users with Python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])