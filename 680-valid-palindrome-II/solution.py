# Runtime: 73ms, Beats 88.46% of users with Python3
# Memory: 16.90MB, Beats 93.35% of users with Python3

class Solution:
    def pali(self,s,l,r):
        while l<r and s[l] == s[r]:
            l+=1
            r-=1
        return l>=r
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                l1 = s[l+1:r+1]
                l2= s[l:r]
                return l1 == l1[::-1] or l2 == l2[::-1]
            l+=1
            r-=1
        return True
