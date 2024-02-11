# Runtime: 77ms, Beats 87.54% of users with Python3
# Memory: 16.69MB, Beats 71.70% of users with Python3

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxf=0
        res=0
        n=len(s)
        count=[0]*26
        for r in range(n):
            count[ord(s[r])-65]+=1
            maxf=max(maxf,count[ord(s[r])-65])
            if(r-l+1-maxf>k):
                count[ord(s[l])-65]-=1
                l+=1
            res=max(res,r-l+1)
        return res