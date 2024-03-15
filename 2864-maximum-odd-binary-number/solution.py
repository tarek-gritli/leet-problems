# Runtime: 52.01% of users with Python3
# Memory: 16.65MB, Beats 17.08% of users with Python3


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=sorted(s,reverse=True)
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                s[i],s[len(s)-1]=s[len(s)-1],s[i]
                break
        return "".join(s)