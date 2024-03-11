# Runtime: 30ms, Beats 87.77% of users with Python3
# Memory: 16.53MB, Beats 61.09% of users with Python3

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch=""
        count={}
        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)
        for i in range(len(order)):
            ch+=order[i]*count.get(order[i],0)
            count[order[i]]-=count.get
        for i in range(len(s)):
            if s[i] not in order:
                ch+=s[i]
        return ch