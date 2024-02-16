# Runtime: 387ms, Beats 44.47% of users with Python3
# Memory: 42.60MB, Beats 6.64% of users with Python3

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        count={}
        n=len(arr)
        for i in range(n):
            count[arr[i]]=1+count.get(arr[i],0)
        count=dict(sorted(count.items(),key=lambda x:x[1]))
        for key,val in count.items():
            count[key]-=min(k,val)
            k-=min(k,val)
            if k==0:
                break
        num=0
        for key,val in count.items():
            if count[key] ==0:
                continue
            num+=1
        return num