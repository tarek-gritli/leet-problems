# Runtime: 32ms, Beats 90.23% of users with Python3
# Memory: 16.54MB, Beats 87.43% of users with Python3

class Solution:
    def myAtoi(self, s):
        s=s.lstrip()
        if len(s) == 0:
            return 0
        ch=""
        k=0
        if s[0] == "-":
            ch+="-"
            k=1
        elif s[0] == "+":
            k=1
        for i in range(k,len(s)):
            if not s[i].isdigit():
                break
            ch+=s[i]
        if ch=="-" or ch=="":
            return 0
        elif int(ch)>2**31-1:
            return 2**31-1
        elif int(ch)<2**31 * -1:
            return 2**31 *-1
        else:
            return int(ch)