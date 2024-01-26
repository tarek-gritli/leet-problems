# Runtime: 24ms, Beats 97.59% of users with Python
# Memory: 13.31MB, Beats 23.57% of users with Python

class Solution(object):
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)
        