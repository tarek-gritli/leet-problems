# Runtime: 87ms, Beats 83.54% of users with Python3
# Memory: 21.18MB, Beats 78.41% of users with Python3

class Solution:
    def topKFrequent(self, nums, k) :
        occ={}
        for el in nums:
            if el in occ.keys():
                occ[el]+=1
            else:
                occ[el]=1
        occ=sorted(occ.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(occ[i][0])
        return res
        