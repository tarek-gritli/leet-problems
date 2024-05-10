# Runtime: 951ms, Beats 49.66% of users with Python3
# Memory: 80.56MB, Beats 37.08% of users with Python3

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        v=[]
        n=len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                v.append([arr[i],arr[j]])
        v.sort(key=lambda x: x[0]/x[1])
        return v[k-1]

