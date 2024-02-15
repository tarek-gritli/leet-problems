# Runtime: 167ms, Beats 73.79% of users with Python3
# Memory: 21.00MB, Beats 69.76% of users with Python3

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while(l<r):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1