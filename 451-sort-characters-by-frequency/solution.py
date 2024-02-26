# Runtime: 60ms, Beats 18.43% of users with Python3
# Memory: 17.73MB, Beats 79.59% of users with Python 3

class Solution:
    def frequencySort(self, s: str) -> str:
        n=len(s)
        count={}
        for i in range(n):
            count[s[i]]=1+count.get(s[i],0)
        count=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        ch=""
        for el,num in count.items():
            ch+=el*num
        return ch