# Runtime: 43ms, Beats 60.41% of users with Python3
# Memory: 16.57MB, Beats 83.74% of users with Python3

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count={}
        maxi=0
        for i in range(len(nums)):
            count[nums[i]]= 1 +count.get(nums[i],0)
            maxi = max(maxi,count[nums[i]])
        res=0
        for key,val in count.items():
            if val == maxi:
                res+=val
        return res