# Runtime: 29ms, Beats 91.76% of users with Python3
# Memory: 16.59MB, Beats 88.75% of users with Python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j+=1
            i+=1
        return j == len(s)