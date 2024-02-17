# Runtime: 274ms, Beats 85.14% of users with Python3
# Memory: 16.66MB, Beats 73.50% of users with Python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength=0
        substring=""
        for i in range(n):
            l,r=i,i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1>maxLength:
                    maxLength=r-l+1
                    substring=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > maxLength:
                    maxLength=r-l+1
                    substring=s[l:r+1]
                l-=1
                r+=1
        return substring