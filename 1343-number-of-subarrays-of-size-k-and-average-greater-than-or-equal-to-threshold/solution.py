# Runtime: 466ms, Beats 39.66% of users with Python3
# Memory: 29.80MB, Beats 83.24% of users with Python3


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr=0
        n=len(arr)
        l,r=0,1
        sum=arr[l]
        while(l<=n-k):
            if(r-l+1<=k):
                sum+=arr[r]
                r+=1
            else:
                if sum >= k*threshold:
                    subarr+=1
                sum-=arr[l]
                l+=1
        return subarr