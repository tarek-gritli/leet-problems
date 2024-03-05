# Runtime: 72ms, Beats 51.66% of users with Python3
# Memory: 17.25MB, Beats 92.89% of users with Python3

class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0,len(s)-1
        while l<r and s[l] == s[r]:
            l+=1
            while l<r and s[l] == s[l-1]:
                l+=1
            r-=1
            while l<r and s[r] == s[r+1]:
                r-=1
        return r-l+1