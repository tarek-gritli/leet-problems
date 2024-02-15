# Runtime: 38ms, Beats 42.53% of users with Python3
# Memory: 16.60MB, Beats 86.16% of users with Python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=len(s)-1
        while(r>=0 and s[r]==" "):
            r-=1
        l=r-1
        while(l>=0 and s[l]!=" "):
            l-=1
        return r-l